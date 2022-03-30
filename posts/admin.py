from django.contrib import admin

from posts.models import Post
from posts.models import Image


@admin.register(Post)
class ProfilesAdmin(admin.ModelAdmin):
    pass

@admin.register(Image)
class ProfilesAdmin(admin.ModelAdmin):
    pass