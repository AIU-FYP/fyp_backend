from django.contrib import admin

from users.models import Profile, User

models = [User, Profile]

for model in models:
    admin.site.register(model)
