from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.

from futbolec.models import Equipo, Jugador, Campeonato, CampeonatoE

# Se crea una clase que hereda
# de ModelAdmin para el modelo
# Estudiante
class EquipoAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str)
    # de la clase
    list_display = ('nombre', 'siglas', 'username')
    search_fields = ('nombre', 'siglas')
# admin.site.register se lo altera
# el primer argumento es el modelo (Estudiante)
# el segundo argumento la clase EstudianteAdmin
admin.site.register(Equipo, EquipoAdmin)

# admin.site.register(Matricula)
class JugadorAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str)
    # de la clase
    list_display = ('nombre', 'posicion', 'nroCamiseta', 'sueldo','equipo')
    search_fields = ('equipo__nombre',)

admin.site.register(Jugador, JugadorAdmin)

class CampeonatoAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str)
    # de la clase
    list_display = ('nombreCampeonato', 'nombreAuspiciante')
    search_fields = ('nombreCampeonato', 'nombreAuspiciante',)

admin.site.register(Campeonato, CampeonatoAdmin)

class CampeonatoEAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str)
    # de la clase
    list_display = ('anio', 'equipo', 'campeonato')
    search_fields = ('equipo__nombre', 'campeonato__nombreCampeonato',)

admin.site.register(CampeonatoE, CampeonatoEAdmin)

