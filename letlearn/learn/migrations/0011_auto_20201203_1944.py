# Generated by Django 3.1.3 on 2020-12-03 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0010_auto_20201129_0114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignmentresult',
            old_name='submitid',
            new_name='uploadid',
        ),
    ]
