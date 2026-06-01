import unittest

from app import create_app


class PurimMonitorTestCase(unittest.TestCase):
    def setUp(self):
        self.client = create_app().test_client()

    def test_home(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["project"], "PurimMonitor")
        self.assertEqual(response.headers["X-Frame-Options"], "DENY")

    def test_health(self):
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "healthy"})

    def test_stats(self):
        response = self.client.get("/stats")
        payload = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIn("cpu_percent", payload)
        self.assertIn("memory_percent", payload)
        self.assertIn("disk_percent", payload)
        self.assertIn("system", payload)
        self.assertIn("hostname", payload)


if __name__ == "__main__":
    unittest.main()
