# Generated by Django 3.1.6 on 2021-02-16 00:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_auto_20210216_0304'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projecttopic',
            old_name='nameproject',
            new_name='nameprojectTopic',
        ),
    ]
