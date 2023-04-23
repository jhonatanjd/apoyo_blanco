# Generated by Django 4.1.5 on 2023-03-08 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_alter_cliente_ciudad_alter_profesional_ciudad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='ciudad',
            field=models.CharField(choices=[('fusagasuga', 'fusagasuga'), ('medellin', 'medellin'), ('facatativa', 'facatativa'), ('el carmen de bolivar', 'el carmen de bolivar'), ('boyaca', 'boyaca'), ('leticia', 'leticia'), ('sabanalarga', 'sabanalarga'), ('barranquilla', 'barranquilla'), ('arauca', 'arauca'), ('cartagena', 'cartagena'), ('tunja', 'tunja'), ('cucuta', 'cucuta'), ('girardot', 'girardot'), ('bogota', 'bogota'), ('zipaquira', 'zipaquira'), ('rionegro', 'rionegro'), ('magangue', 'magangue'), ('cali', 'cali'), ('turbo', 'turbo'), ('apartado', 'apartado'), ('caucasia', 'caucasia')], max_length=40),
        ),
        migrations.AlterField(
            model_name='profesional',
            name='ciudad',
            field=models.CharField(choices=[('fusagasuga', 'fusagasuga'), ('medellin', 'medellin'), ('facatativa', 'facatativa'), ('el carmen de bolivar', 'el carmen de bolivar'), ('boyaca', 'boyaca'), ('leticia', 'leticia'), ('sabanalarga', 'sabanalarga'), ('barranquilla', 'barranquilla'), ('arauca', 'arauca'), ('cartagena', 'cartagena'), ('tunja', 'tunja'), ('cucuta', 'cucuta'), ('girardot', 'girardot'), ('bogota', 'bogota'), ('zipaquira', 'zipaquira'), ('rionegro', 'rionegro'), ('magangue', 'magangue'), ('cali', 'cali'), ('turbo', 'turbo'), ('apartado', 'apartado'), ('caucasia', 'caucasia')], max_length=40),
        ),
        migrations.AlterField(
            model_name='profesional',
            name='especialidad',
            field=models.CharField(choices=[('Neonatología', 'Neonatología'), ('Enfermería_de_familia', 'Enfermería_de_familia'), ('Nefrología', 'Nefrología'), ('Atención_primaria', 'Atención_primaria'), ('Geriatría', 'Geriatría'), ('Urgencias', 'Urgencias'), ('Pediatría', 'Pediatría'), ('Cardiología', 'Cardiología'), ('Salud_escolar', 'Salud_escolar'), ('Oncología', 'Oncología'), ('Salud_de_la_mujer', 'Salud_de_la_mujer')], max_length=40),
        ),
        migrations.AlterField(
            model_name='profesional',
            name='grado_estudio',
            field=models.CharField(choices=[('Especialización_tecnica', 'Especialización_tecnica'), ('tecnologo', 'tecnologo'), ('tecnico', 'tecnico'), ('profesional', 'profesional'), ('Especialización_profesional', 'Especialización_profesional'), ('Especialización_tecnologica', 'Especialización_tecnologica')], max_length=40),
        ),
    ]
