import argparse
import json
import re
from collections import Counter
from pathlib import Path


HTTP_LOG_PATTERN = re.compile(
    r'(?P<ip>\S+)\s+\S+\s+\S+\s+\[(?P<timestamp>[^\]]+)\]\s+'
    r'"(?P<method>[A-Z]+)\s+(?P<path>\S+)\s+(?P<protocol>[^"]+)"\s+'
    r'(?P<status>\d{3})\s+(?P<size>\S+)'
)
LEVEL_PATTERN = re.compile(r"\b(?P<level>DEBUG|INFO|WARNING|WARN|ERROR|CRITICAL|FATAL)\b", re.IGNORECASE)
DEFAULT_TOP_LIMIT = 5


def normalize_level(level):
    upper = level.upper()

    if upper == "WARN":
        return "WARNING"
    if upper == "FATAL":
        return "CRITICAL"

    return upper


def parse_log_line(line):
    """Parse a single log line into a normalized event dictionary."""
    line = line.rstrip("\n")
    http_match = HTTP_LOG_PATTERN.search(line)

    if http_match:
        payload = http_match.groupdict()
        size = payload["size"]
        return {
            "type": "http",
            "ip": payload["ip"],
            "timestamp": payload["timestamp"],
            "method": payload["method"],
            "path": payload["path"],
            "protocol": payload["protocol"],
            "status": int(payload["status"]),
            "size": None if size == "-" else int(size),
            "raw": line,
        }

    level_match = LEVEL_PATTERN.search(line)

    return {
        "type": "text",
        "level": normalize_level(level_match.group("level")) if level_match else None,
        "raw": line,
    }


def analyze_lines(lines, top_limit=DEFAULT_TOP_LIMIT):
    """Return useful operational summaries from an iterable of log lines."""
    events = [parse_log_line(line) for line in lines if line.strip()]
    http_events = [event for event in events if event["type"] == "http"]
    text_events = [event for event in events if event["type"] == "text"]

    status_counts = Counter(str(event["status"]) for event in http_events)
    method_counts = Counter(event["method"] for event in http_events)
    path_counts = Counter(event["path"] for event in http_events)
    level_counts = Counter(
        event["level"]
        for event in text_events
        if event["level"] is not None
    )

    error_lines = [
        event["raw"]
        for event in text_events
        if event["level"] in {"ERROR", "CRITICAL"}
    ][:top_limit]

    return {
        "total_lines": len(events),
        "http_requests": len(http_events),
        "text_events": len(text_events),
        "status_counts": dict(sorted(status_counts.items())),
        "method_counts": dict(method_counts.most_common(top_limit)),
        "top_paths": dict(path_counts.most_common(top_limit)),
        "level_counts": dict(level_counts.most_common()),
        "error_samples": error_lines,
    }


def analyze_file(path, top_limit=DEFAULT_TOP_LIMIT):
    with Path(path).open("r", encoding="utf-8") as handle:
        return analyze_lines(handle, top_limit=top_limit)


def format_summary(summary):
    lines = [
        "LogLens Summary",
        "===============",
        f"Total lines: {summary['total_lines']}",
        f"HTTP requests: {summary['http_requests']}",
        f"Text events: {summary['text_events']}",
    ]

    if summary["status_counts"]:
        lines.append(f"HTTP status counts: {summary['status_counts']}")

    if summary["method_counts"]:
        lines.append(f"HTTP methods: {summary['method_counts']}")

    if summary["top_paths"]:
        lines.append(f"Top paths: {summary['top_paths']}")

    if summary["level_counts"]:
        lines.append(f"Log levels: {summary['level_counts']}")

    if summary["error_samples"]:
        lines.append("Error samples:")
        lines.extend(f"- {line}" for line in summary["error_samples"])

    return "\n".join(lines)


def build_parser():
    parser = argparse.ArgumentParser(description="Summarize HTTP and application log files.")
    parser.add_argument("path", help="Path to the log file to analyze.")
    parser.add_argument("--top", type=int, default=DEFAULT_TOP_LIMIT, help="Number of top paths/errors to show.")
    parser.add_argument("--json", action="store_true", help="Output machine-readable JSON.")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)

    if args.top < 1:
        raise SystemExit("--top must be greater than zero")

    summary = analyze_file(args.path, top_limit=args.top)

    if args.json:
        print(json.dumps(summary, indent=2, sort_keys=True))
    else:
        print(format_summary(summary))


if __name__ == "__main__":
    main()
