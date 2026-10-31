from django.template import response
from django.test import TestCase


#import your tests here
class APITests(TestCase):

    def test_hello_endpoint(self):
        response = self.client.get("/api/hello/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json()["message"],
            "Hello from CSC 325!"
        )
    def test_status_endpoint(self):
        response = self.client.get("/api/status/")

        self.assertEqual(response.status_code, 200)

        self.assertEqual(
            response.json()["status"],
            "running"
        )

        self.assertEqual(
            response.json()["version"],
            "2.0"
        )