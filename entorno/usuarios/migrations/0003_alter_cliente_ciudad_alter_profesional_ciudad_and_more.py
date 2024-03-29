# Generated by Django 4.1.5 on 2023-03-08 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_alter_cliente_ciudad_alter_profesional_ciudad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='ciudad',
            field=models.CharField(choices=[('cucuta', 'cucuta'), ('facatativa', 'facatativa'), ('bogota', 'bogota'), ('medellin', 'medellin'), ('leticia', 'leticia'), ('cartagena', 'cartagena'), ('zipaquira', 'zipaquira'), ('magangue', 'magangue'), ('turbo', 'turbo'), ('boyaca', 'boyaca'), ('sabanalarga', 'sabanalarga'), ('girardot', 'girardot'), ('apartado', 'apartado'), ('arauca', 'arauca'), ('rionegro', 'rionegro'), ('caucasia', 'caucasia'), ('el carmen de bolivar', 'el carmen de bolivar'), ('tunja', 'tunja'), ('cali', 'cali'), ('fusagasuga', 'fusagasuga'), ('barranquilla', 'barranquilla')], max_length=40),
        ),
        migrations.AlterField(
            model_name='profesional',
            name='ciudad',
            field=models.CharField(choices=[('cucuta', 'cucuta'), ('facatativa', 'facatativa'), ('bogota', 'bogota'), ('medellin', 'medellin'), ('leticia', 'leticia'), ('cartagena', 'cartagena'), ('zipaquira', 'zipaquira'), ('magangue', 'magangue'), ('turbo', 'turbo'), ('boyaca', 'boyaca'), ('sabanalarga', 'sabanalarga'), ('girardot', 'girardot'), ('apartado', 'apartado'), ('arauca', 'arauca'), ('rionegro', 'rionegro'), ('caucasia', 'caucasia'), ('el carmen de bolivar', 'el carmen de bolivar'), ('tunja', 'tunja'), ('cali', 'cali'), ('fusagasuga', 'fusagasuga'), ('barranquilla', 'barranquilla')], max_length=40),
        ),
        migrations.AlterField(
            model_name='profesional',
            name='especialidad',
            field=models.CharField(choices=[('Enfermería_de_familia', 'Enfermería_de_familia'), ('Pediatría', 'Pediatría'), ('Neonatología', 'Neonatología'), ('Salud_de_la_mujer', 'Salud_de_la_mujer'), ('Atención_primaria', 'Atención_primaria'), ('Cardiología', 'Cardiología'), ('Geriatría', 'Geriatría'), ('Urgencias', 'Urgencias'), ('Oncología', 'Oncología'), ('Salud_escolar', 'Salud_escolar'), ('Nefrología', 'Nefrología')], max_length=40),
        ),
        migrations.AlterField(
            model_name='profesional',
            name='grado_estudio',
            field=models.CharField(choices=[('tecnologo', 'tecnologo'), ('Especialización_tecnica', 'Especialización_tecnica'), ('Especialización_tecnologica', 'Especialización_tecnologica'), ('tecnico', 'tecnico'), ('Especialización_profesional', 'Especialización_profesional'), ('profesional', 'profesional')], max_length=40),
        ),
    ]
