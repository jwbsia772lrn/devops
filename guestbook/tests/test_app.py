import unittest

import app as guestbook


class GuestbookTestCase(unittest.TestCase):
    def setUp(self):
        guestbook.app.config.update(TESTING=True)
        guestbook._memory_entries.clear()
        self.client = guestbook.app.test_client()

    def test_health(self):
        response = self.client.get("/healthz")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["status"], "ok")

    def test_add_and_read(self):
        response = self.client.post(
            "/add",
            data={"name": "student", "message": "hello"},
        )
        self.assertEqual(response.status_code, 302)

        entries_response = self.client.get("/api/entries")
        self.assertEqual(entries_response.status_code, 200)
        data = entries_response.get_json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["entries"][0]["message"], "hello")


if __name__ == "__main__":
    unittest.main()
