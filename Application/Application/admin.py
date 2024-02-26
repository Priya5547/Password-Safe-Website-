from django.contrib import admin
from Application.models import User_db , Password_db
# Register your models here.

admin.site.register(User_db)
admin.site.register(Password_db)
