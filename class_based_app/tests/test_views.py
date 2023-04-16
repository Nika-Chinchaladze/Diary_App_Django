from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from class_based_app.views import Diary


class TestView(TestCase):
    def setUp(self):
        self.logout_url = reverse("logout")
        self.new = reverse("new")
        self.user_image = reverse("user-image")
        self.back_image = reverse("back-image")
        self.detail = reverse("detail", kwargs={"pk": 1})
        self.update = reverse("update", kwargs={"pk": 1})
        self.delete = reverse("delete", kwargs={"pk": 1})
        self.all = reverse("all")
    


class TestLoginView(TestCase):
    
    def setUp(self):
        self.login_url = reverse("login")
        self.client = Client()
    
    # we test view's url, if view exists at desired location
    def test_login_view_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    # we test view, if it is accessible by name
    def test_login_view_name(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
    
    # we test view, if it uses correct template
    def test_login_view_template(self):
        response = self.client.get(self.login_url)
        self.assertTemplateUsed(response, "diary_app/login.html")
    

class TestRegisterView(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse("register")
    
    # we test view's url, if view exists at desired location
    def test_register_view_location(self):
        response = self.client.get("/register")
        self.assertEqual(response.status_code, 200)
    
    # we test view, if it is accessible by name
    def test_register_view_name(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
    
    # we test view, if it uses correct template
    def test_register_view_template(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)


class TestHomeView(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_view_url = reverse("home")

        # create users
        self.first_user = User.objects.create_user(username="chincho", password="12345678")
        self.second_user = User.objects.create_user(username="lazvi", password="12345678")
        self.first_user.save()
        self.second_user.save()

        # create Diaries
        quantity = 5
        for i in range(quantity):
            chosen_user = self.first_user if quantity % 2 == 0 else self.second_user
            Diary.objects.create(
                title=f"extreme rock climbing {i}",
                content=f"don't hurry! {i}",
                image_url=f"https://www.youtube.com/{i}",
                user=chosen_user
            )

    # we test, if view redirects when user is not logged in
    def test_home_view_redirect_not_logged_in(self):
        response = self.client.get(self.home_view_url)
        self.assertRedirects(response, "/?next=/home")

    # we test, if logged in view uses correct template
    def test_logged_in_home_view_correct_template(self):
        self.client.login(username="chincho", password="12345678")
        response = self.client.get(self.home_view_url)

        # here we check if user is logged in, response is 'success' and correct template is rendered
        self.assertEqual(str(response.context["user"].username), self.first_user.username)
        self.assertEqual(str(response.context["user"].password), self.first_user.password)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "diary_app/home.html")
    
    # we test, if view - context data return diaries that belongs to logged in user
    def test_view_only_returns_users_diaries(self):
        self.client.login(username="chincho", password="12345678")
        response = self.client.get(self.home_view_url)

        # check: user is logged in
        self.assertEqual(str(response.context["user"].username), self.first_user.username)
        # check: we get 'success' response
        self.assertEqual(response.status_code, 200)
        # check: we have correct context name
        self.assertTrue("notes" in response.context)
        # check: we have zero diaries initially
        self.assertEqual(len(response.context["notes"]), 0)

        # desired diaries
        diaries = Diary.objects.filter(user=self.first_user).all()

        # check: we get only those diaries that belong to logged in user
        for diary in diaries:
            self.assertEqual(diary.user.username, self.first_user.username)


        

