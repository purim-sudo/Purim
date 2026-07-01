import unittest

from app import VERSION, create_app


class PurimMonitorTestCase(unittest.TestCase):
    def setUp(self):
        self.client = create_app().test_client()

    def test_home(self):
        response = self.client.get("/")
        payload = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(payload["project"], "PurimMonitor")
        self.assertEqual(payload["version"], VERSION)
        self.assertEqual(payload["runtime"], "python")
        self.assertEqual(response.headers["X-Frame-Options"], "DENY")

    def test_health(self):
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "healthy", "version": VERSION})

    def test_version(self):
        response = self.client.get("/version")
        payload = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(payload["project"], "PurimMonitor")
        self.assertEqual(payload["version"], VERSION)
        self.assertIn("python_version", payload)

    def test_stats(self):
        response = self.client.get("/stats")
        payload = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIn("cpu_percent", payload)
        self.assertIn("memory_percent", payload)
        self.assertIn("disk_percent", payload)
        self.assertIn("system", payload)
        self.assertIn("release", payload)
        self.assertIn("hostname", payload)
        self.assertIn("python_version", payload)
        self.assertIn("boot_time_unix", payload)
        self.assertIn("uptime_seconds", payload)
        self.assertIn("load_average", payload)


if __name__ == "__main__":
    unittest.main()
