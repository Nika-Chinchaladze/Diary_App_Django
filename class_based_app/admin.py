from django.contrib import admin
from .models import Diary, Image, Background


# Register your models here.
class DiaryAdmin(admin.ModelAdmin):
    list_display = ("title", "date_time", "content", "image_url", "user",)


class ImageAdmin(admin.ModelAdmin):
    list_display = ("image", "user",)


class BackgroundAdmin(admin.ModelAdmin):
    list_display = ("image", "user",)


admin.site.register(Diary, DiaryAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Background, BackgroundAdmin)
