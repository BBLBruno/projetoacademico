# Generated by Django 5.1.3 on 2024-12-17 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_area_saber_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matriculas',
            old_name='matricula',
            new_name='nome',
        ),
    ]
