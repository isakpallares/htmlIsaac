from django.contrib import admin

# Register your models here.
from Aplicacion1.models import Estudiantes, Materias, Cursos

class EstudiantesAdmin(admin.ModelAdmin):
    list_display=("nombre", "edad")
    search_fields=('nombre','edad')
    list_filter=('nombre',) #No olvidar Coma
# class MateriasAdmin(admin.ModelAdmin):
#     list_display=("materia", ["estudiantes"])
#     search_fields=('materia')
#     list_filter=('materia',) #No olvidar Coma
# class CursosAdmin(admin.ModelAdmin):
#     list_display=("curso", "cantidadEstudiantes")
#     search_fields=(['curso'])
#     list_filter=('curso',) #No olvidar Coma

admin.site.register(Estudiantes,EstudiantesAdmin)
admin.site.register(Materias)
admin.site.register(Cursos)
    