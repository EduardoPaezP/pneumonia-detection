# Generated by Django 4.2.16 on 2024-12-05 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_remove_informe_id_analisis_remove_paciente_id_medico_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='altura',
            field=models.FloatField(),
        ),
    ]
