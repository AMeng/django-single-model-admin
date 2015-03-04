from singlemodeladmin import SingleModelAdmin
from django.contrib import admin
from app.models import TestModel

admin.site.register(TestModel, SingleModelAdmin)
