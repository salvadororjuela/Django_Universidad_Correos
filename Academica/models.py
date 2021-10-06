from django.db import models


# Create your models here.
# Tabla de Carreras
class Carreras(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=50)
    duracion = models.PositiveSmallIntegerField(default=5)

    # Vuelve legible la informacion de la carrera en el administrador
    def __str__(self):
        return f"{self.codigo}: {self.nombre}. Duracion: {self.duracion} años"


# Tabla de Estudiantes
class Estudiantes(models.Model):
    cedula = models.CharField(max_length=8, primary_key=True)
    primerApellido = models.CharField(max_length=35)
    segundoApellido = models.CharField(max_length=35)
    nombres = models.CharField(max_length=35)
    fechaNacimiento = models.DateField()
    sexos = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]
    # choices toma los valores de la lista sexos (arriba declarada)
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    carrera = models.ForeignKey(
        Carreras, null=False, blank=False, on_delete=models.CASCADE)
    vigencia = models.BooleanField(default=True)

    def __str__(self):
        # Establece VIGENTE o DE BAJA de acuerdo con la vigencia del estudiante
        if self.vigencia:
            estadoEstudiante = "VIGENTE"
        else:
            estadoEstudiante = "DE BAJA"

        return f"Estudiante: {self.primerApellido} {self.segundoApellido}, {self.nombres}. Carrera: {self.carrera}. Estado: {estadoEstudiante}"


# Tabla de Cursos
class Cursos(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)
    nombre = models.CharField(max_length=30)
    creditos = models.PositiveSmallIntegerField()
    docente = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.codigo}: {self.nombre}. Creditos: {self.creditos}. Docente: {self.docente}"


# Tabla Matriculas
class Matriculas(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(
        Estudiantes, null=False, blank=False, on_delete=models.CASCADE)
    curso = models.ForeignKey(
        Cursos, null=False, blank=False, on_delete=models.CASCADE)
    # auto_now_add guarda automaticamente hora y fecha actual
    fechaMatricula = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.estudiante.sexo == "F":
            letraSexo = "a"
        else:
            letraSexo = "o"

        fechMat = self.fechaMatricula.strftime("%m/%d/%Y %H:%M")

        return f"{self.id}: {self.estudiante}. Curso: {self.curso}. Matricula{letraSexo}: {fechMat}"
