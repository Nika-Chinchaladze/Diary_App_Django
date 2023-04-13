from django.test import TestCase
from django.contrib.auth.models import User

from class_based_app.models import Diary, Image, Background


class TestDiaryModel(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username="chincharito")
        Diary.objects.create(
            title="Tommy Shelby",
            content="By order of the peacky blinders!!!",
            image_url="https://www.youtube.com",
            user=user
        )
    
    def setUp(self):
        self.note = Diary.objects.get(id=1)
    
    # Here we test labels for all model-fields to find out if they have values that we desire.
    def test_title_label(self):
        field_label = self.note._meta.get_field("title").verbose_name
        self.assertEqual(field_label, "title")
    
    def test_date_time_label(self):
        field_label = self.note._meta.get_field("date_time").verbose_name
        self.assertEqual(field_label, "date time")
    
    def test_content_label(self):
        field_label = self.note._meta.get_field("content").verbose_name
        self.assertEqual(field_label, "content")
    
    def test_image_url_label(self):
        field_label = self.note._meta.get_field("image_url").verbose_name
        self.assertEqual(field_label, "image url")
    
    def test_user_label(self):
        field_label = self.note._meta.get_field("user").verbose_name
        self.assertEqual(field_label, "user")
    
    # here we test model fields on maximum length to see if they meet requirements.
    def test_title_max_length(self):
        max_length = self.note._meta.get_field("title").max_length
        self.assertEqual(max_length, 200)
    
    def test_image_url_max_length(self):
        max_length = self.note._meta.get_field("image_url").max_length
        self.assertEqual(max_length, 500)
    
    def test_object_name_str_look(self):
        expected_object_name = f"{self.note.title} {self.note.date_time} {self.note.content} {self.note.image_url} {self.note.user}"
        self.assertEqual(str(self.note), expected_object_name)


