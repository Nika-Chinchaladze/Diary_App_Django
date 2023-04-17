from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

from class_based_app.views import Diary, Image, Background


class TestView(TestCase):
    def setUp(self):
        self.new = reverse("new")
        self.user_image = reverse("user-image")
        self.back_image = reverse("back-image")
        self.update = reverse("update", kwargs={"pk": 1})
        self.delete = reverse("delete", kwargs={"pk": 1})
    


class TestLoginView(TestCase):
    
    def setUp(self):
        self.login_url = reverse("login")
        self.client = Client()
        self.my_user = User.objects.create_user(username="lazvi", password="12345678")
    
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
    
    # we test view, if valid data is posted correctly
    def test_login_view_post_valid_data(self):
        my_data = {
            "username": "lazvi",
            "password": "12345678"
        }
        response = self.client.post(reverse("login"), my_data)
        self.assertRedirects(response, reverse("home"))
    
    # we test view, if invalid data is catched and redirected to login page again
    def test_login_view_post_invalid_data(self):
        my_data = {
            "username": "nika",
            "password": "chinchaladze"
        }
        response = self.client.post(reverse("login"), my_data)
        self.assertRedirects(response, self.login_url)
    

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

    @classmethod
    def setUpTestData(cls):
        my_user_1 = User.objects.create_user(username="lazvi", password="12345678")
        my_user_2 = User.objects.create_user(username="chincho", password="12345678")
        my_user_1.save()
        my_user_2.save()

        # upload user's profile image
        image_path = "media/images/nata.jpg"
        Image.objects.create(
            image=SimpleUploadedFile(
                name="tested_profile.jpg",
                content=open(image_path, "rb").read(),
                content_type="images/jpeg"
            ),
            user=my_user_1
        )

        # upload user's background image
        background_path = "media/images/sea.jpg"
        Background.objects.create(
            image=SimpleUploadedFile(
                name="tested_background.jpg",
                content=open(background_path, "rb").read(),
                content_type="images/jpeg"
            ),
            user=my_user_1
        )

        # create Diaries
        quantity = 5
        for i in range(quantity):
            chosen_user = my_user_1 if i % 2 == 0 else my_user_2
            Diary.objects.create(
                title=f"extreme rock climbing {i}",
                content=f"don't hurry! {i}",
                image_url=f"https://www.youtube.com/{i}",
                user=chosen_user
            )


    def setUp(self):
        self.client = Client()
        self.home_view_url = reverse("home")

    # we test view's url, if view exists at desired location
    def test_home_view_desired_location(self):
        self.client.login(username="lazvi", password="12345678")
        response = self.client.get("/home")
        self.assertEqual(response.status_code, 200)

    # we test view, if it is accessible by name
    def test_home_view_by_name(self):
        self.client.login(username="lazvi", password="12345678")
        response = self.client.get(self.home_view_url)
        self.assertEqual(response.status_code, 200)

    # we test, if view redirects to login page when user is not logged-in
    def test_home_view_redirect_not_logged_in(self):
        response = self.client.get(self.home_view_url)
        self.assertRedirects(response, "/?next=/home")

    # we test, if logged in view uses correct template
    def test_logged_in_home_view_correct_template(self):
        self.client.login(username="lazvi", password="12345678")
        response = self.client.get(self.home_view_url)

        # chosen user
        chosen_user = User.objects.filter(username="lazvi").first()

        # here we check if user is logged in, response is 'success' and correct template is rendered
        self.assertEqual(str(response.context["user"].username), chosen_user.username)
        self.assertEqual(str(response.context["user"].password), chosen_user.password)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "diary_app/home.html")
    
    # we test, if view - context data return diaries that belongs to logged in user
    def test_view_returns_users_diaries_profile_and_background_images(self):
        self.client.login(username="lazvi", password="12345678")
        response = self.client.get(self.home_view_url)

        # chosen user
        chosen_user = User.objects.filter(username="lazvi").first()

        # check: user is logged in
        self.assertEqual(str(response.context["user"].username), chosen_user.username)
        # check: we get 'success' response
        self.assertEqual(response.status_code, 200)
        # check: we have correct context name
        self.assertTrue("notes" in response.context)

        # desired context data: diaries, profile image, background image
        diaries = Diary.objects.filter(user=chosen_user).all()

        profile_image = Image.objects.filter(user=chosen_user).first()
        background_image = Background.objects.filter(user=chosen_user).first()

        # check: we get only those diaries that belong to logged-in user
        for diary in diaries:
            self.assertEqual(diary.user.username, chosen_user.username)
        
        # check: we test, if user sees his/her profile image
        self.assertEqual(profile_image.user.username, chosen_user.username)

        # check: we test, if user sees his/her background/theme image
        self.assertEqual(background_image.user.username, chosen_user.username)

    # here we test, if diary notes returned by view is ordered in descending order
    def test_diary_notes_in_descending_order(self):
        self.client.login(username="lazvi", password="12345678")
        response = self.client.get(self.home_view_url)
        chosen_user = User.objects.filter(username="lazvi").first()
        notes = Diary.objects.filter(user=chosen_user).all()
        view_notes = [note.date_time for note in notes]
        check_point = view_notes
        check_point.sort(reverse=True)
        self.assertEqual(view_notes, check_point)
        self.assertEqual(response.status_code, 200)



class TestLogoutView(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username="chincho", password="12345678")
    
    def setUp(self):
        self.client = Client()
        self.logout_url = reverse("logout")
        
    # we test view's url, if view exists at desired location
    def test_logout_view_desired_location(self):
        self.client.login(username="chincho", password="12345678")
        response = self.client.get("/logout")
        self.assertEqual(response.status_code, 200)

    # we test view, if it is accessible by name
    def test_logout_view_by_name(self):
        self.client.login(username="chincho", password="12345678")
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 200)
    
    # we test view, if it uses correct template
    def test_logout_view_used_template(self):
        self.client.login(username="chincho", password="12345678")
        response = self.client.get(self.logout_url)

        # here we check if user is logged in, response is 'success' and correct template is rendered
        self.assertTrue(response.context["user"].username is None or response.context["user"].username == "")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "diary_app/logout.html")
    
    # we test, if view redirects to login page when user is not logged-in
    def test_logout_view_redirects_not_logged_in_user(self):
        response = self.client.get(self.logout_url)
        self.assertRedirects(response, "/?next=/logout")



class TestNoteDetailView(TestCase):

    @classmethod
    def setUpTestData(cls):
        my_user = User.objects.create_user(username="chincho", password="12345678")
        Diary.objects.create(
            title="Title",
            content="Content",
            image_url="https://www.youtube.com",
            user=my_user
        )

    def setUp(self):
        self.client = Client()
        self.detail_url = reverse("detail", kwargs={"pk": 1})
    
    # we test view's url, if view exists at desired location
    def test_detail_view_desired_location(self):
        self.client.login(username="chincho", password="12345678")
        response = self.client.get("/detail/1")
        self.assertEqual(response.status_code, 200)
    
    # we test view, if it is accessible by name
    def test_detail_view_by_name(self):
        self.client.login(username="chincho", password="12345678")
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
    
    # we test view, if it uses correct template
    def test_detail_view_used_template(self):
        self.client.login(username="chincho", password="12345678")
        response = self.client.get(self.detail_url)

        # chosen user
        chosen_user = User.objects.filter(username="chincho").first()

        # here we check if user is logged in, response is 'success' and correct template is rendered
        self.assertTemplateUsed(response, "diary_app/detail.html")
        self.assertEqual(response.context["user"].username, chosen_user.username)
        self.assertEqual(response.status_code, 200)

    # we test, if view redirects to login page when user is not logged-in
    def test_detail_view_redirects_not_logged_in_user(self):
        response = self.client.get(self.detail_url)
        self.assertRedirects(response, "/?next=/detail/1")

    # we test, if view - context data returns correct note that belongs to logged-in user
    def test_detail_view_return_correct_context_data(self):
        self.client.login(username="chincho", password="12345678")
        response = self.client.get(self.detail_url)

        # currect user & chosen note details
        current_user = User.objects.filter(username="chincho").first()
        chosen_note = Diary.objects.filter(user=current_user).first()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(chosen_note.user.username, current_user.username)



class TestNoteListView(TestCase):

    @classmethod
    def setUpTestData(cls):
        my_user = User.objects.create_user(username="chincho", password="12345678")
        for i in range(5):
            Diary.objects.create(
                title=f"Title {i}",
                content=f"Content {i}",
                image_url=f"https://www.youtube.com/{i}",
                user=my_user
            )

    def setUp(self):
        self.client = Client()
        self.all_url = reverse("all")

    # we test view's url, if view exists at desired location
    def test_all_view_desired_location(self):
        self.client.login(username="chincho", password="12345678")
        response = self.client.get("/all")
        self.assertEqual(response.status_code, 200)
    
    # we test view, if it is accessible by name
    def test_all_view_by_name(self):
        self.client.login(username="chincho", password="12345678")
        response = self.client.get(self.all_url)
        self.assertEqual(response.status_code, 200)
    
    # we test view, if it uses correct template
    def test_all_view_used_template(self):
        self.client.login(username="chincho", password="12345678")
        response = self.client.get(self.all_url)

        # current user
        currect_user = User.objects.filter(username="chincho").first()

        # here we check if user is logged in, response is 'success' and correct template is rendered
        self.assertEqual(response.context["user"].username, currect_user.username)
        self.assertTemplateUsed(response, "diary_app/all.html")
        self.assertTrue(response.status_code, 200)
    
    # we test, if view redirects to login page when user is not logged-in
    def test_all_view_redirects_not_logged_in_users(self):
        response = self.client.get(self.all_url)
        self.assertRedirects(response, "/?next=/all")

    # we test, if view - context data returns correct note that belongs to logged-in user
    def test_all_view_returns_correct_context_data(self):
        self.client.login(username="chincho", password="12345678")
        response = self.client.get(self.all_url)

        # current user
        current_user = User.objects.filter(username="chincho").first()
        user_notes = Diary.objects.filter(user=current_user).all()

        for note in user_notes:
            self.assertEqual(note.user, current_user)
        self.assertEqual(response.status_code, 200)
    
    # here we test, if diary notes returned by view is ordered in descending order
    def test_all_view_returns_context_data_in_descending_order(self):
        self.client.login(username="chincho", password="12345678")
        response = self.client.get(self.all_url)
        current_user = User.objects.filter(username="chincho").first()
        notes = Diary.objects.filter(user=current_user).all()
        user_notes = [note.date_time for note in notes]
        check_point_notes = user_notes
        check_point_notes.sort(reverse=True)
        self.assertEqual(user_notes, check_point_notes)
        self.assertEqual(response.status_code, 200)



class TestAddNoteView(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username="chincho", password="12345678")

    def setUp(self):
        self.client = Client()
        self.new_url = reverse("new")
    
    # we test view's url, if view exists at desired location
    def test_new_view_desired_location(self):
        self.client.login(username="chincho", password="12345678")
        response = self.client.get("/new")
        self.assertEqual(response.status_code, 200)

    # we test view, if it is accessible by name
    def test_new_view_by_name(self):
        self.client.login(username="chincho", password="12345678")
        response = self.client.get(self.new_url)
        self.assertEqual(response.status_code, 200)

    # we test view, if it uses correct template
    def test_new_view_used_template(self):
        self.client.login(username="chincho", password="12345678")
        response = self.client.get(self.new_url)
        self.assertTemplateUsed(response, "diary_app/new.html")

    # we test, if view redirects to login page when user is not logged-in
    def test_new_view_redirects_not_logged_in_user(self):
        response = self.client.get(self.new_url)
        self.assertRedirects(response, "/?next=/new")
    
    # we test, post valid data
    def test_new_view_post_form(self):
        self.client.login(username="chincho", password="12345678")
        current_user = User.objects.filter(username="chincho").first()
        my_data = {
            "title": "famous peacky blinders",
            "image_url": "https://www.youtube.com/1",
            "content": "by order of the peacky blinders",
            "user": current_user
        }
        response = self.client.post(self.new_url, data=my_data)

        # check post results:
        all_notes = Diary.objects.filter(user=current_user).count()
        print(all_notes)

