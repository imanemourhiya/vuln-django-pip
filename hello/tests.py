from django.test import TestCase


class IndexTests(TestCase):
    def test_index_returns_ok(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")
