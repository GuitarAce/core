# Generated by Django 2.1.15 on 2021-02-03 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassPj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namepj', models.CharField(max_length=50)),
                ('listname', models.CharField(max_length=50)),
                ('professor', models.CharField(max_length=50)),
            ],
        ),
    ]
