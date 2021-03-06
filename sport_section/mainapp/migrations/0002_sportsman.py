# Generated by Django 2.2 on 2021-06-06 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sportsman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.TextField(max_length=128)),
                ('name', models.TextField(max_length=128)),
                ('age', models.IntegerField(default=0)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.SectionView')),
            ],
            options={
                'verbose_name': 'Спортсмен',
                'verbose_name_plural': 'Спортсмены',
            },
        ),
    ]
