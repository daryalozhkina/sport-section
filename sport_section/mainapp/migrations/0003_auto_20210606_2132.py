# Generated by Django 2.2 on 2021-06-06 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_sportsman'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sportsman',
            old_name='group',
            new_name='section',
        ),
    ]
