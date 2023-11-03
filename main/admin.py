from django.contrib import admin
from .models import studentModel,teachersModel,courseModel,booksModel


# Register your models here.
admin.site.register(studentModel)
admin.site.register(teachersModel)
admin.site.register(courseModel)
admin.site.register(booksModel)


