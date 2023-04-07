from django.test import TestCase, SimpleTestCase

# Create your tests here.


class SimpleTests(SimpleTestCase):
    def test_login_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_logout_page_status_code(self):
        response = self.client.get("/logout")
        self.assertEqual(response.status_code, 302)
    
    def test_register_page_status_code(self):
        response = self.client.get("/register")
        self.assertEqual(response.status_code, 200)

    def test_home_page_status_code(self):
        response = self.client.get("/home")
        self.assertEqual(response.status_code, 200)
