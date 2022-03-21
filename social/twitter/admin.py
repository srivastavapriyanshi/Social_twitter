from django.contrib import admin
from .models import Profile, Tweets

# Register your models here.
from django.contrib.auth.models import User, Group

class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    # Only display the "username" field
    fields = ["username"]
    inlines = [ProfileInline]
    

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Tweets)
admin.site.unregister(Group)
