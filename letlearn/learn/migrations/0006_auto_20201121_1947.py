# Generated by Django 2.2.17 on 2020-11-21 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0005_auto_20201121_1938'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignmentresult',
            old_name='assignmentresultname',
            new_name='assignmentresult',
        ),
        migrations.AddField(
            model_name='calender',
            name='calender',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
