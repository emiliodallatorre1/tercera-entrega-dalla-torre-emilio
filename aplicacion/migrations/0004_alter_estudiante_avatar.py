# Generated by Django 5.0.6 on 2024-07-24 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_alter_estudiante_materias_alter_materia_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars_estudiantes/'),
        ),
    ]
