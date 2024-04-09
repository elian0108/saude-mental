from django.contrib import admin

from app.models import Form, MedicalRecord, Patient, Question

# Register your models here.
admin.site.register(Patient)
admin.site.register(MedicalRecord)
admin.site.register(Form)
admin.site.register(Question)