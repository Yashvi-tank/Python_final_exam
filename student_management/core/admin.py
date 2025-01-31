from django.contrib import admin
from .models import Student, Subject, Grade  

# Registering models so they appear in the admin panel
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Grade)