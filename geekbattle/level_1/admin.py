from django.contrib import admin
from .models import Answer
from .models import Question
# Register your models here.

admin.site.register(Answer)
admin.site.register(Question)

