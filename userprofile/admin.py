from userprofile.models import Profile
from django.contrib import admin

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ("first_name", "middle_name", "last_name", "contact", "address")