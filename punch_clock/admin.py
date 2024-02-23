from django.apps import apps
from django.contrib import admin
from django.contrib.auth.models import Group, User

# Register your models here.

# Obtenir tous les models de toutes les applications installees
models = apps.get_models()

admin.site.unregister(Group)
admin.site.unregister(User)

for model in models:
    admin.site.register(model)


