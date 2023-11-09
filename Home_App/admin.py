from django.contrib import admin

from .forms import ImageForm
from .models import BookNow, Comment, Image, Menu

# Register your models here.
admin.site.register(BookNow)
admin.site.register(Comment)
admin.site.register(Menu)


class ImageAdmin(admin.ModelAdmin):
    form = ImageForm


admin.site.register(Image, ImageAdmin)
