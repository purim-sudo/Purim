import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import loglens


class LogLensTestCase(unittest.TestCase):
    def test_parse_http_log_line(self):
        event = loglens.parse_log_line(
            '10.0.0.1 - - [01/Jul/2026:10:00:00 +0300] "GET /health HTTP/1.1" 200 42'
        )

        self.assertEqual(event["type"], "http")
        self.assertEqual(event["method"], "GET")
        self.assertEqual(event["path"], "/health")
        self.assertEqual(event["status"], 200)
        self.assertEqual(event["size"], 42)

    def test_parse_text_log_line_with_level(self):
        event = loglens.parse_log_line("2026-07-01 10:00:00 WARN disk space low")

        self.assertEqual(event["type"], "text")
        self.assertEqual(event["level"], "WARNING")

    def test_analyze_lines_combines_http_and_text_events(self):
        summary = loglens.analyze_lines(
            [
                '10.0.0.1 - - [01/Jul/2026:10:00:00 +0300] "GET / HTTP/1.1" 200 10',
                '10.0.0.1 - - [01/Jul/2026:10:01:00 +0300] "POST /login HTTP/1.1" 500 99',
                "2026-07-01 10:02:00 ERROR database timeout",
                "2026-07-01 10:03:00 INFO recovered",
            ]
        )

        self.assertEqual(summary["total_lines"], 4)
        self.assertEqual(summary["http_requests"], 2)
        self.assertEqual(summary["text_events"], 2)
        self.assertEqual(summary["status_counts"], {"200": 1, "500": 1})
        self.assertEqual(summary["method_counts"], {"GET": 1, "POST": 1})
        self.assertEqual(summary["level_counts"], {"ERROR": 1, "INFO": 1})
        self.assertEqual(summary["error_samples"], ["2026-07-01 10:02:00 ERROR database timeout"])

    def test_analyze_file_reads_utf8_log_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            log_file = Path(temp_dir) / "app.log"
            log_file.write_text("2026-07-01 INFO started\n", encoding="utf-8")

            summary = loglens.analyze_file(log_file)

        self.assertEqual(summary["total_lines"], 1)
        self.assertEqual(summary["level_counts"], {"INFO": 1})

    @mock.patch("builtins.print")
    def test_main_outputs_json(self, print_mock):
        with tempfile.TemporaryDirectory() as temp_dir:
            log_file = Path(temp_dir) / "access.log"
            log_file.write_text(
                '10.0.0.1 - - [01/Jul/2026:10:00:00 +0300] "GET / HTTP/1.1" 200 10\n',
                encoding="utf-8",
            )

            loglens.main([str(log_file), "--json"])

        payload = json.loads(print_mock.call_args.args[0])
        self.assertEqual(payload["http_requests"], 1)


if __name__ == "__main__":
    unittest.main()
