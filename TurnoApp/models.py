from django.db import models

# Create your models here.

class Paciente(models.Model):

    dni = models.PositiveIntegerField(
        primary_key = True,
        db_column = 'DNI'
    )

    nombre = models.CharField(
        max_length = 64,
        db_column = 'NOMBRE'
    )

    apellido = models.CharField(
        max_length = 64,
        db_column = 'APELLIDO'
    )

    class Meta:
        db_table = 'PACIENTE'  


class Turno(models.Model):

    id = models.PositiveIntegerField(
        primary_key = True,
        db_column = 'ID_TURNO'
    )

    fecha_y_hora = models.DateField(
        db_column = 'FECHA_Y_HORA'
    )

    especialista = models.ForeignKey(
        'Especialista',
        on_delete = models.SET_NULL,
        null = True,
        db_column = 'ESPECIALISTA'
    )

    paciente = models.ForeignKey(
        'Paciente',
        on_delete = models.CASCADE,
        db_column = 'PACIENTE'
    )

    tipo_de_atencion = models.ForeignKey(
        'TipoDeAtencion',
        on_delete = models.SET_NULL,
        null = True,
        db_column = 'TIPO_DE_ATENCION'
    )

    class Meta:
        db_table = 'TURNO'  


class Especialista(models.Model):

    matricula = models.PositiveIntegerField(
        primary_key = True,
        db_column = 'NUMERO_MATRICULA'
    )

    nombre = models.CharField(
        max_length = 64,
        db_column = 'NOMBRE'
    )

    apellido = models.CharField(
        max_length = 64,
        db_column = 'APELLIDO'
    )

    tipo_atenciones = models.ManyToManyField(
        'TipoDeAtencion',
        related_name='especialistas'
    )

    class Meta:
        db_table = 'ESPECIALISTA' 


class TipoDeAtencion(models.Model):

    id = models.PositiveIntegerField(
        primary_key = True,
        db_column = 'ID_TURNO'
    )

    nombre = models.CharField(
        max_length = 64,
        db_column = 'NOMBRE'
    )

    descripcion = models.CharField(
        max_length = 256,
        db_column = 'DESCRIPCION'
    )

    class Meta:
        db_table = 'TIPO_DE_ATENCION' 
