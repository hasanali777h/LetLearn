# Generated by Django 3.1.3 on 2020-11-28 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20201127_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
        migrations.AddField(
            model_name='course',
            name='assignto',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='imagelink',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='course',
            name='longdes',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='schoolimage',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='student',
            name='classid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.tblclass'),
        ),
        migrations.AddField(
            model_name='student',
            name='schoolid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.school'),
        ),
        migrations.AddField(
            model_name='student',
            name='sectionid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.section'),
        ),
        migrations.AddField(
            model_name='tblclass',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]