# Generated by Django 5.0.4 on 2024-04-09 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='question',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='medicalrecord',
            name='form_id',
        ),
        migrations.AddField(
            model_name='form',
            name='questions',
            field=models.ManyToManyField(to='app.question', verbose_name='Perguntas'),
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='forms',
            field=models.ManyToManyField(to='app.form', verbose_name='Formularios'),
        ),
        migrations.RemoveField(
            model_name='question',
            name='form_id',
        ),
    ]
