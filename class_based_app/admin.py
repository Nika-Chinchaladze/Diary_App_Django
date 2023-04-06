from django.contrib import admin
from .models import Diary


# Register your models here.
class DiaryAdmin(admin.ModelAdmin):
    list_display = ["title", "date_time", "content", "user"]


admin.site.register(Diary, DiaryAdmin)