from django.contrib import admin
from .models import UserModel
from level_1.models import user_details
# Register your models here.

admin.site.register(UserModel)
admin.site.register(user_details)
# Register your models here.
