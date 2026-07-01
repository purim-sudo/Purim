import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import portal_check


class PortalCheckTestCase(unittest.TestCase):
    def test_review_lines_detects_project_signals(self):
        report = portal_check.review_lines([
            "Portal login page with custom logo",
            "Addressing notes include pool and dns setup",
            "Voucher plans include daily and weekly quotas",
            "Payment notes are ready",
        ])

        self.assertEqual(report["summary"]["total_lines"], 4)
        self.assertEqual(report["summary"]["passed"], 5)
        self.assertEqual(report["summary"]["missing"], 0)

    def test_review_lines_reports_missing_groups(self):
        report = portal_check.review_lines(["Only a login page has been drafted"])

        names = {check["name"]: check for check in report["checks"]}
        self.assertTrue(names["portal"]["ok"])
        self.assertFalse(names["payments"]["ok"])

    def test_review_file_reads_text(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            notes_file = Path(temp_dir) / "notes.txt"
            notes_file.write_text("voucher plan ready\n", encoding="utf-8")

            report = portal_check.review_file(notes_file)

        names = {check["name"]: check for check in report["checks"]}
        self.assertTrue(names["billing"]["ok"])

    def test_format_report_contains_status_labels(self):
        report = portal_check.review_lines(["portal login ready"])
        formatted = portal_check.format_report(report)

        self.assertIn("PortalCheck Report", formatted)
        self.assertIn("[FOUND] portal", formatted)
        self.assertIn("[MISSING] payments", formatted)

    @mock.patch("builtins.print")
    def test_main_outputs_json(self, print_mock):
        with tempfile.TemporaryDirectory() as temp_dir:
            notes_file = Path(temp_dir) / "notes.txt"
            notes_file.write_text("payment notes ready\n", encoding="utf-8")

            portal_check.main([str(notes_file), "--json"])

        payload = json.loads(print_mock.call_args.args[0])
        self.assertEqual(payload["summary"]["total_checks"], 5)


if __name__ == "__main__":
    unittest.main()
