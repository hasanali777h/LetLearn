# Generated by Django 2.2.17 on 2020-11-21 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0003_auto_20201121_1932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submitassignment',
            name='id',
        ),
        migrations.AlterField(
            model_name='submitassignment',
            name='uploadid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
