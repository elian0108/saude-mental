# Generated by Django 5.0.4 on 2024-04-08 23:08

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('diagnostic', models.CharField(max_length=255)),
                ('result', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Formulario',
                'verbose_name_plural': 'Formularios',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateTimeField(default=django.utils.timezone.now)),
                ('CEP', models.CharField(max_length=8)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=20)),
                ('sexo', models.CharField(max_length=1)),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
            },
        ),
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Do_you_accept_contact', models.IntegerField()),
                ('form_id', models.CharField(blank=True, max_length=255, null=True)),
                ('last_test_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.patient')),
            ],
            options={
                'verbose_name': 'Porntuario',
                'verbose_name_plural': 'Porntuarios',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=255)),
                ('value', models.IntegerField()),
                ('form_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.form')),
            ],
            options={
                'verbose_name': 'Pergunta',
                'verbose_name_plural': 'Perguntas',
                'unique_together': {('form_id', 'id')},
            },
        ),
    ]