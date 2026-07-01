import argparse
import json
from collections import Counter
from pathlib import Path


DEFAULT_KEYWORDS = {
    "portal": ("portal", "hotspot", "login", "landing"),
    "addressing": ("dhcp", "pool", "gateway", "dns"),
    "branding": ("html", "logo", "template", "brand"),
    "billing": ("voucher", "plan", "profile", "quota"),
    "payments": ("mpesa", "stk", "callback", "payment"),
}


def normalize_line(line):
    return line.strip().lower()


def review_lines(lines, keyword_groups=None):
    keyword_groups = keyword_groups or DEFAULT_KEYWORDS
    normalized = [normalize_line(line) for line in lines if line.strip()]
    counters = Counter()
    samples = {group: [] for group in keyword_groups}

    for line in normalized:
        for group, keywords in keyword_groups.items():
            if any(keyword in line for keyword in keywords):
                counters[group] += 1
                if len(samples[group]) < 3:
                    samples[group].append(line)

    checks = []
    for group in keyword_groups:
        count = counters[group]
        checks.append({
            "name": group,
            "ok": count > 0,
            "matches": count,
            "samples": samples[group],
        })

    passed = sum(1 for check in checks if check["ok"])

    return {
        "summary": {
            "total_lines": len(normalized),
            "total_checks": len(checks),
            "passed": passed,
            "missing": len(checks) - passed,
        },
        "checks": checks,
    }


def review_file(path):
    with Path(path).open("r", encoding="utf-8") as handle:
        return review_lines(handle)


def format_report(report):
    lines = [
        "PortalCheck Report",
        "==================",
        f"Lines reviewed: {report['summary']['total_lines']}",
        f"Signals found: {report['summary']['passed']}/{report['summary']['total_checks']}",
        "",
    ]

    for check in report["checks"]:
        status = "FOUND" if check["ok"] else "MISSING"
        lines.append(f"[{status}] {check['name']} ({check['matches']} matches)")
        for sample in check["samples"]:
            lines.append(f"  - {sample}")

    return "\n".join(lines)


def build_parser():
    parser = argparse.ArgumentParser(description="Review exported portal setup notes for common project signals.")
    parser.add_argument("path", help="Path to a text export, notes file, or setup checklist.")
    parser.add_argument("--json", action="store_true", help="Output JSON instead of a text report.")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    report = review_file(args.path)

    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print(format_report(report))


if __name__ == "__main__":
    main()
