from django.test import SimpleTestCase
from django.urls import reverse, resolve
from class_based_app import views


class TestUrls(SimpleTestCase):
    def test_login_url_is_resolved(self):
        url = reverse("login")
        self.assertEqual(resolve(url).func.__name__, views.LoginView.as_view().__name__)
    
    def test_logout_url_is_resolved(self):
        url = reverse("logout")
        self.assertEqual(resolve(url).func.__name__, views.LogoutView.as_view().__name__)
    
    def test_register_url_is_resolved(self):
        url = reverse("register")
        self.assertEqual(resolve(url).func.__name__, views.RegisterView.as_view().__name__)
    
    def test_home_url_is_resolved(self):
        url = reverse("home")
        self.assertEqual(resolve(url).func.__name__, views.HomeView.as_view().__name__)
    
    def test_new_url_is_resolved(self):
        url = reverse("new")
        self.assertEqual(resolve(url).func.__name__, views.AddNoteView.as_view().__name__)
    
    def test_user_image_url_is_resolved(self):
        url = reverse("user-image")
        self.assertEqual(resolve(url).func.__name__, views.AddImageView.as_view().__name__)
    
    def test_back_image_url_is_resolved(self):
        url = reverse("back-image")
        self.assertEqual(resolve(url).func.__name__, views.AddBackgroundView.as_view().__name__)
    
    def test_detail_url_is_resolved(self):
        url = reverse("detail", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.__name__, views.NoteDetailView.as_view().__name__)
    
    def test_update_url_is_resolved(self):
        url = reverse("update", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.__name__, views.NoteUpdateView.as_view().__name__)
    
    def test_delete_url_is_resolved(self):
        url = reverse("delete", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, views.NoteDeleteView)
    
    def test_all_url_is_resolved(self):
        url = reverse("all")
        self.assertEqual(resolve(url).func.__name__, views.NoteListView.as_view().__name__)
