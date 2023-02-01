# Generated by Django 4.1.5 on 2023-02-01 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='adduser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=20)),
                ('Last_Name', models.CharField(max_length=20)),
                ('user', models.CharField(max_length=15)),
                ('password', models.TextField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(max_length=30)),
            ],
        ),
    ]
