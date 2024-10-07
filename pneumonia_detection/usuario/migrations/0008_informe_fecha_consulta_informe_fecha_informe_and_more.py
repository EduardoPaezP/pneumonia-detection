# Generated by Django 4.2.16 on 2024-10-06 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0007_alter_analisis_recomendaciones_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='informe',
            name='fecha_consulta',
            field=models.DateField(default='2024-09-28'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='informe',
            name='fecha_informe',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='informe',
            name='recomendaciones',
            field=models.TextField(max_length=1000),
        ),
    ]
