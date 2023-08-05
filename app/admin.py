from django.contrib import admin
""" para añadir nuestros modelos creados en nuestro panel de admin DJANGO """
from .models import Project, Task

# Register your models here.
admin.site.register(Project)
admin.site.register(Task)