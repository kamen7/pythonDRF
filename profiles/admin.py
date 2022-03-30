from django.contrib import admin

from profiles.models import Profile
from profiles.models import Contacts


@admin.register(Profile)
class ProfilesAdmin(admin.ModelAdmin):
    pass


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    pass


