import socket
import unittest
from argparse import ArgumentTypeError
from unittest import mock

import scanner
import subnet_scan


class ScannerTestCase(unittest.TestCase):
    def test_parse_ports(self):
        self.assertEqual(scanner.parse_ports("22, 80,443"), (22, 80, 443))

    def test_parse_ports_rejects_invalid_values(self):
        with self.assertRaises(ArgumentTypeError):
            scanner.parse_ports("0")

    @mock.patch("scanner.check_port")
    def test_scan_ports(self, check_port):
        check_port.side_effect = [True, False]

        results = scanner.scan_ports("127.0.0.1", (80, 443), timeout=0.1)

        self.assertEqual(results[0], {"host": "127.0.0.1", "port": 80, "open": True})
        self.assertEqual(results[1], {"host": "127.0.0.1", "port": 443, "open": False})


class SubnetScanTestCase(unittest.TestCase):
    @mock.patch("subnet_scan.resolve_host")
    def test_scan_subnet(self, resolve_host):
        resolve_host.side_effect = ["router.local", None]

        results = subnet_scan.scan_subnet("192.168.1.0/30")

        self.assertEqual(
            results,
            [
                {"ip": "192.168.1.1", "hostname": "router.local"},
                {"ip": "192.168.1.2", "hostname": None},
            ],
        )

    @mock.patch("subnet_scan.socket.gethostbyaddr")
    def test_resolve_host_missing(self, gethostbyaddr):
        gethostbyaddr.side_effect = socket.herror()

        self.assertIsNone(subnet_scan.resolve_host("192.168.1.10"))


if __name__ == "__main__":
    unittest.main()
