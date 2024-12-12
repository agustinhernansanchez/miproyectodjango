# Generated by Django 4.2.17 on 2024-12-12 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('fecha_publicacion', models.DateField()),
                ('autor', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=13)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Periodico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('fecha_publicacion', models.DateField()),
                ('seccion', models.CharField(max_length=100)),
                ('editor', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Revista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('fecha_publicacion', models.DateField()),
                ('numero', models.IntegerField()),
                ('editorial', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
