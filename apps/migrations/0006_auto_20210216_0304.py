# Generated by Django 3.1.6 on 2021-02-15 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_auto_20210215_1354'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameproject', models.CharField(max_length=50)),
                ('listproject', models.CharField(max_length=50)),
                ('professorname', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='ClassProject',
        ),
    ]
