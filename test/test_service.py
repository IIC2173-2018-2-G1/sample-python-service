import unittest

from src.main import app


class BasicTests(unittest.TestCase):

    # executed prior to each test
    def setUp(self):
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        app.config["DEBUG"] = False
        self.app = app.test_client()

        self.assertEqual(app.debug, False)

    def test_todos_page(self):
        response = self.app.get("/todos", follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_missing_parameter(self):
        response = self.app.put("/todos/1", follow_redirects=True)
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
