from django.test import TestCase, Client
from django.urls import reverse



class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse("login")
        self.logout_url = reverse("logout")
        self.register = reverse("register")
        self.home = reverse("home")
        self.new = reverse("new")
        self.user_image = reverse("user-image")
        self.back_image = reverse("back-image")
        self.detail = reverse("detail", kwargs={"pk": 1})
        self.update = reverse("update", kwargs={"pk": 1})
        self.delete = reverse("delete", kwargs={"pk": 1})
        self.all = reverse("all")
    
    def test_login_GET(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "diary_app/login.html")
    