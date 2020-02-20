from unittest import TestCase
from app import create_app


class TestScore(TestCase):
    def test_score(self):
        app = create_app()
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)

    def test_match(self):
        app = create_app()
        tester = app.test_client(self)
        response = tester.get('/match')
        self.assertEqual(response.status_code, 401)
