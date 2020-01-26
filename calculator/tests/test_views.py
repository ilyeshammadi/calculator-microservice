import unittest

from pyramid import testing

from calculator.views.default import add


class AddViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_can_add(self):
        request = testing.DummyRequest(
            path='/add', json_body={"a": 1, "b": 1})
        response = add(request)
        self.assertEqual(response.json_body['result'], 2)
        self.assertEqual(response.status_code, 200)

    def test_can_not_add(self):
        request = testing.DummyRequest(
            path='/add', json_body={"a": 1})
        response = add(request)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json_body, {"message": "Invalid arguments"})
