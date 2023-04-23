# Generated by Django 4.1.5 on 2023-03-08 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_alter_cliente_ciudad_alter_profesional_ciudad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='ciudad',
            field=models.CharField(choices=[('rionegro', 'rionegro'), ('zipaquira', 'zipaquira'), ('medellin', 'medellin'), ('arauca', 'arauca'), ('cartagena', 'cartagena'), ('facatativa', 'facatativa'), ('girardot', 'girardot'), ('cali', 'cali'), ('sabanalarga', 'sabanalarga'), ('el carmen de bolivar', 'el carmen de bolivar'), ('turbo', 'turbo'), ('caucasia', 'caucasia'), ('cucuta', 'cucuta'), ('magangue', 'magangue'), ('leticia', 'leticia'), ('barranquilla', 'barranquilla'), ('apartado', 'apartado'), ('boyaca', 'boyaca'), ('tunja', 'tunja'), ('bogota', 'bogota'), ('fusagasuga', 'fusagasuga')], max_length=40),
        ),
        migrations.AlterField(
            model_name='profesional',
            name='ciudad',
            field=models.CharField(choices=[('rionegro', 'rionegro'), ('zipaquira', 'zipaquira'), ('medellin', 'medellin'), ('arauca', 'arauca'), ('cartagena', 'cartagena'), ('facatativa', 'facatativa'), ('girardot', 'girardot'), ('cali', 'cali'), ('sabanalarga', 'sabanalarga'), ('el carmen de bolivar', 'el carmen de bolivar'), ('turbo', 'turbo'), ('caucasia', 'caucasia'), ('cucuta', 'cucuta'), ('magangue', 'magangue'), ('leticia', 'leticia'), ('barranquilla', 'barranquilla'), ('apartado', 'apartado'), ('boyaca', 'boyaca'), ('tunja', 'tunja'), ('bogota', 'bogota'), ('fusagasuga', 'fusagasuga')], max_length=40),
        ),
        migrations.AlterField(
            model_name='profesional',
            name='especialidad',
            field=models.CharField(choices=[('Atención_primaria', 'Atención_primaria'), ('Enfermería_de_familia', 'Enfermería_de_familia'), ('Salud_de_la_mujer', 'Salud_de_la_mujer'), ('Urgencias', 'Urgencias'), ('Oncología', 'Oncología'), ('Neonatología', 'Neonatología'), ('Geriatría', 'Geriatría'), ('Pediatría', 'Pediatría'), ('Cardiología', 'Cardiología'), ('Salud_escolar', 'Salud_escolar'), ('Nefrología', 'Nefrología')], max_length=40),
        ),
        migrations.AlterField(
            model_name='profesional',
            name='grado_estudio',
            field=models.CharField(choices=[('tecnologo', 'tecnologo'), ('profesional', 'profesional'), ('Especialización_tecnologica', 'Especialización_tecnologica'), ('tecnico', 'tecnico'), ('Especialización_profesional', 'Especialización_profesional'), ('Especialización_tecnica', 'Especialización_tecnica')], max_length=40),
        ),
    ]