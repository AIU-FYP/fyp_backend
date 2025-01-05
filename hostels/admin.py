from django.contrib import admin

from hostels.models import Hostel, Level, Room, Bed

models = [Hostel, Level, Room, Bed]

for model in models:
    admin.site.register(model)