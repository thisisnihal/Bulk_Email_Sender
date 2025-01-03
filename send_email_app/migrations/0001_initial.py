# Generated by Django 5.1.4 on 2024-12-29 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Desgination', models.CharField(max_length=30)),
            ],
        ),
    ]
