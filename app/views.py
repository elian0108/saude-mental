from django.shortcuts import render

# Create your views here.
from .models import Patient, Question, Form, MedicalRecord

#@login_required(login_url='/login/')
def index(request):
    if request.method == 'POST':
        # Aqui você pode processar os dados do formulário
        pass
    else:
        perguntas = Question.objects.all()
        formularios = Form.objects.all()
        pacientes = Patient.objects.all()
        prontuarios = MedicalRecord.objects.all()
        context = {
            'perguntas': perguntas,
            'formularios': formularios,
            'pacientes': pacientes,
            'prontuarios': prontuarios,
        }
        return render(request, 'form.html', context)
    