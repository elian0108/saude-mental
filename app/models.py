from django.db import models
from django.utils import timezone
# Create your models here.

class Patient(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255, null=False)
  date_of_birth = models.DateTimeField(default=timezone.now)
  CEP = models.CharField(max_length=8, null=False)
  email = models.EmailField(null=False)
  telefone = models.CharField(max_length=20, null=False)
  sexo = models.CharField(max_length=1, null=False)

  def __str__(self):
        return self.name

  class Meta:
    verbose_name = "Paciente"
    verbose_name_plural = "Pacientes"

class MedicalRecord(models.Model):
  id = models.AutoField(primary_key=True)
  Do_you_accept_contact = models.IntegerField(null=False)
  patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
  form_id = models.CharField(max_length=255, null=True, blank=True)
  last_test_date = models.DateTimeField(default=timezone.now)

  def __str__(self):
        return self.name

  class Meta:
    verbose_name = "Porntuario"
    verbose_name_plural = "Porntuarios"
 
class Form(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255, null=False)
  diagnostic = models.CharField(max_length=255, null=False)
  result = models.IntegerField(null=False)

  def __str__(self):
        return self.name

  class Meta:
    verbose_name = "Formulario"
    verbose_name_plural = "Formularios"

class Question(models.Model):
  id = models.AutoField(primary_key=True)
  form_id = models.ForeignKey(Form, on_delete=models.CASCADE) 
  question = models.CharField(max_length=255, null=False)
  value = models.IntegerField(null=False)

  def __str__(self):
        return self.name

  class Meta:
    verbose_name = "Pergunta"
    verbose_name_plural = "Perguntas"
    unique_together = (('form_id', 'id'),)  # Define composite primary key