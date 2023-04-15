from django.test import TestCase, SimpleTestCase
from django.contrib.auth.models import User

from class_based_app.forms import LoginForm, RegistrationForm, DiaryModelForm, ImageModelForm, BackgroundModelForm


class TestLoginForm(SimpleTestCase):

    def setUp(self):
        self.form = LoginForm()

    # here we test, if form has fields, that we are expecting.
    def test_login_form_fields_existence(self):
        form_fields = list(self.form.fields.keys())
        expected_fields = ["username", "password"]
        self.assertEqual(form_fields, expected_fields)

    # here we test, if form fields have desired label, that we are expecting.
    def test_login_username_label(self):
        my_field = self.form.fields["username"]
        self.assertTrue(my_field.label is None or my_field.label == "")
    
    def test_login_password_label(self):
        my_field = self.form.fields["password"]
        self.assertTrue(my_field.label is None or my_field.label == "")
    
    # here we test, if form fields have desired placeholder text, that we are expecting.
    def test_login_username_placeholder(self):
        my_field = self.form.fields["username"]
        self.assertEqual(my_field.widget.attrs["placeholder"], "username")
    
    def test_login_password_placeholder(self):
        my_field = self.form.fields["password"]
        self.assertEqual(my_field.widget.attrs["placeholder"], "password")

    # here we test, max length of form field - if they work properly.
    def test_login_username_max_length(self):
        my_field = self.form.fields["username"]
        self.assertEqual(my_field.max_length, 150)
    
    def test_login_password_max_length(self):
        my_field = self.form.fields["password"]
        self.assertEqual(my_field.max_length, 150)
    
    # here we test, form validation.
    def test_login_username_validation(self):
        my_username = "a" * 200
        my_password = "chincho"
        my_form = LoginForm(data={"username": my_username, "password": my_password})
        self.assertFalse(my_form.is_valid())
    
    def test_login_password_validation(self):
        my_username = "chincho"
        my_password = "a" * 200
        my_form = LoginForm(data={"username": my_username, "password": my_password})
        self.assertFalse(my_form.is_valid())



class TestRegistrationForm(TestCase):

    def setUp(self):
        self.form = RegistrationForm()

    # here we test, if form has fields, that we are expecting.
    def test_register_fields(self):
        form_fields = list(self.form.fields)
        expected_fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
        self.assertEqual(form_fields, expected_fields)

    # here we test, if form fields have desired label, that we are expecting.
    def test_register_username_label(self):
        my_field = self.form.fields["username"]
        self.assertTrue(my_field.label is None or my_field.label == "")
    
    def test_register_first_name_label(self):
        my_field = self.form.fields["first_name"]
        self.assertTrue(my_field.label is None or my_field.label == "")
    
    def test_register_last_name_label(self):
        my_field = self.form.fields["last_name"]
        self.assertTrue(my_field.label is None or my_field.label == "")
    
    def test_register_email_label(self):
        my_field = self.form.fields["email"]
        self.assertTrue(my_field.label is None or my_field.label == "")
    
    def test_register_password1_label(self):
        my_field = self.form.fields["password1"]
        self.assertTrue(my_field.label is None or my_field.label == "")
    
    def test_register_password2_label(self):
        my_field = self.form.fields["password2"]
        self.assertTrue(my_field.label is None or my_field.label == "")

    # here we test, if form fields have desired placeholder text, that we are expecting.
    def test_register_username_placeholder(self):
        my_field = self.form.fields["username"]
        self.assertEqual(my_field.widget.attrs["placeholder"], "username")
    
    def test_register_first_name_placeholder(self):
        my_field = self.form.fields["first_name"]
        self.assertEqual(my_field.widget.attrs["placeholder"], "first name")
    
    def test_register_last_name_placeholder(self):
        my_field = self.form.fields["last_name"]
        self.assertEqual(my_field.widget.attrs["placeholder"], "last name")
    
    def test_register_email_placeholder(self):
        my_field = self.form.fields["email"]
        self.assertEqual(my_field.widget.attrs["placeholder"], "email")
    
    def test_register_password1_placeholder(self):
        my_field = self.form.fields["password1"]
        self.assertEqual(my_field.widget.attrs["placeholder"], "password 1")
    
    def test_register_password2_placeholder(self):
        my_field = self.form.fields["password2"]
        self.assertEqual(my_field.widget.attrs["placeholder"], "password 2")

    # here we test, max length of form field - if they work properly.
    def test_register_username_max_length(self):
        my_field = self.form.fields["username"]
        self.assertEqual(my_field.max_length, 150)
    
    def test_register_first_name_max_length(self):
        my_field = self.form.fields["first_name"]
        self.assertEqual(my_field.max_length, 150)
    
    def test_register_last_name_max_length(self):
        my_field = self.form.fields["last_name"]
        self.assertEqual(my_field.max_length, 150)
    
    def test_register_email_max_length(self):
        my_field = self.form.fields["email"]
        self.assertEqual(my_field.max_length, 150)
    
    def test_register_password1_max_length(self):
        my_field = self.form.fields["password1"]
        self.assertEqual(my_field.max_length, 150)
    
    def test_register_password2_max_length(self):
        my_field = self.form.fields["password2"]
        self.assertEqual(my_field.max_length, 150)

    # here we test, form validation
    def test_register_username_validation(self):
        form_data = {
            "username": "a" * 200,
            "first_name": "Nika",
            "last_name": "Chinchaladze",
            "email": "chincho@gmail.com",
            "password1": "Contact12@",
            "password2": "Contact12@"
        }
        my_form = RegistrationForm(data=form_data)
        self.assertFalse(my_form.is_valid())
    
    def test_register_first_name_validation(self):
        form_data = {
            "username": "chincharito",
            "first_name": "a" * 200,
            "last_name": "Chinchaladze",
            "email": "chincho@gmail.com",
            "password1": "Contact12@",
            "password2": "Contact12@"
        }
        my_form = RegistrationForm(data=form_data)
        self.assertFalse(my_form.is_valid())
    
    def test_register_last_name_validation(self):
        form_data = {
            "username": "chincharito",
            "first_name": "Nika",
            "last_name": "a" * 200,
            "email": "chincho@gmail.com",
            "password1": "Contact12@",
            "password2": "Contact12@"
        }
        my_form = RegistrationForm(data=form_data)
        self.assertFalse(my_form.is_valid())
    
    def test_register_email_validation(self):
        form_data = {
            "username": "chincharito",
            "first_name": "Nika",
            "last_name": "Chinchaladze",
            "email": "a" * 200,
            "password1": "Contact12@",
            "password2": "Contact12@"
        }
        my_form = RegistrationForm(data=form_data)
        self.assertFalse(my_form.is_valid())
    
    def test_register_password1_validation(self):
        form_data = {
            "username": "chincharito",
            "first_name": "Nika",
            "last_name": "Chinchaladze",
            "email": "chincho@gmail.com",
            "password1": "a" * 200,
            "password2": "Contact12@"
        }
        my_form = RegistrationForm(data=form_data)
        self.assertFalse(my_form.is_valid())
    
    def test_register_password2_validation(self):
        form_data = {
            "username": "chincharito",
            "first_name": "Nika",
            "last_name": "Chinchaladze",
            "email": "chincho@gmail.com",
            "password1": "Contact12@",
            "password2": "a" * 200
        }
        my_form = RegistrationForm(data=form_data)
        self.assertFalse(my_form.is_valid())
    
    def test_register_password_similarity_validation(self):
        form_data = {
            "username": "chincharito",
            "first_name": "Nika",
            "last_name": "Chinchaladze",
            "email": "chincho@gmail.com",
            "password1": "Contact12@",
            "password2": "Contact12@"
        }
        my_form = RegistrationForm(data=form_data)
        self.assertTrue(my_form.is_valid())
    
    def test_register_password_non_similarity_validation(self):
        form_data = {
            "username": "chincharito",
            "first_name": "Nika",
            "last_name": "Chinchaladze",
            "email": "chincho@gmail.com",
            "password1": "First12@",
            "password2": "Second12@"
        }
        my_form = RegistrationForm(data=form_data)
        self.assertFalse(my_form.is_valid())
    


class TestDiaryModelForm(TestCase):

    def setUp(self):
        self.form = DiaryModelForm()
    
    # here we test, if form has fields, that we are expecting.
    def test_diary_fields(self):
        form_fields = list(self.form.fields)
        expected_fields = ["title", "image_url", "content", "user"]
        self.assertEqual(form_fields, expected_fields)

    # here we test, if form fields have desired label, that we are expecting.
    def test_diary_title_label(self):
        my_field = self.form.fields["title"]
        self.assertTrue(my_field.label is None or my_field.label == "")
    
    def test_diary_image_url_label(self):
        my_field = self.form.fields["image_url"]
        self.assertTrue(my_field.label is None or my_field.label == "")
    
    def test_diary_content_label(self):
        my_field = self.form.fields["content"]
        self.assertTrue(my_field.label is None or my_field.label == "")
    
    def test_diary_user_label(self):
        my_field = self.form.fields["user"]
        self.assertTrue(my_field.label is None or my_field.label == "Author")

    # here we test, if form fields have desired placeholder text, that we are expecting.
    def test_diary_title_placeholder(self):
        my_field = self.form.fields["title"]
        self.assertEqual(my_field.widget.attrs["placeholder"], "Title")
    
    def test_diary_image_url_placeholder(self):
        my_field = self.form.fields["image_url"]
        self.assertEqual(my_field.widget.attrs["placeholder"], "Image Link")
    
    def test_diary_content_placeholder(self):
        my_field = self.form.fields["content"]
        self.assertEqual(my_field.widget.attrs["placeholder"], "Diary Content")

    # here we test, max length of form field - if they work properly.
    def test_diary_title_max_length(self):
        my_field = self.form.fields["title"]
        self.assertEqual(my_field.max_length, 200)
    
    def test_diary_image_url_length(self):
        my_field = self.form.fields["image_url"]
        self.assertEqual(my_field.max_length, 500)

    # here we test, form validation
    def test_diary_title_validation(self):
        my_data = {
            "title": "a" * 300,
            "image_url": "https://www.youtube.com",
            "content": "Peacky Blinders",
            "user": User.objects.create(username="chincho")
        }
        my_form = DiaryModelForm(data=my_data)
        self.assertFalse(my_form.is_valid())
    
    def test_diary_image_url_validation(self):
        my_data = {
            "title": "Extreme Rock Climbing",
            "image_url": f"https://www.youtube.com/{'a' * 500}",
            "content": "Peacky Blinders",
            "user": User.objects.create(username="chincho")
        }
        my_form = DiaryModelForm(data=my_data)
        self.assertFalse(my_form.is_valid())



class TestImageModelForm(TestCase):

    def setUp(self):
        self.form = ImageModelForm()

    # here we test, if form has fields, that we are expecting.
    def test_image_fields(self):
        form_fields = list(self.form.fields)
        expected_fields = ["image", "user"]
        self.assertEqual(form_fields, expected_fields)
    
    



