from django.contrib import admin
from .models import Carreras, Estudiantes, Cursos, Matriculas


# Register your models here.
admin.site.register(Carreras)
admin.site.register(Estudiantes)
admin.site.register(Cursos)
admin.site.register(Matriculas)
