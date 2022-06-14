from django.db import models

# Create your models here.

class Equipo(models.Model):

    nombre = models.CharField("Nombre del equipo", max_length=30)
    siglas = models.CharField("Siglas", max_length=30)  # el campo puede
                                                            # ser vacio
    username = models.CharField(max_length=30, unique=True)
   

    def __str__(self):
        return "%s  - %s - Username Twitter: %s" % (self.nombre,
                self.siglas,
                self.username)


class Jugador(models.Model):
    """
    """
    nombre = models.CharField(max_length=30)
    posicion = models.CharField(max_length=30, unique=True)
    nroCamiseta = models.CharField(max_length=30, unique=True)
    sueldo = models.CharField(max_length=30)
    equipo = models.ForeignKey(Equipo, related_name='losjugadores',
            on_delete=models.CASCADE)


    def __str__(self):
        return "Jugador: %s - %s - %s - %s - %s" % (self.nombre,
        self.posicion,
        self.nroCamiseta,
        self.sueldo,
        self.equipo.nombre)


class Campeonato(models.Model):
    """
    """
    nombreCampeonato = models.CharField(max_length=30)
    nombreAuspiciante = models.CharField(max_length=30)

    equipos = models.ManyToManyField(Equipo, through='CampeonatoE')

   
    def __str__(self):
        return "Campeonato: Nombre de Campeonato(%s) - Nombre del Auspiciante(%s)" % \
                (self.nombreCampeonato, self.nombreAuspiciante)

class CampeonatoE(models.Model):
    """
    """
    anio = models.CharField(max_length=200)
    equipo = models.ForeignKey(Equipo, related_name='loscampeonatos',
            on_delete=models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, related_name='loscampeonatos',
            on_delete=models.CASCADE)

    def __str__(self):
        return "Matricula: Año(%s) - Equipo de Fútbol(%s) - Campeonato(%s)" % \
                (self.anio, self.equipo.nombre, self.campeonato)