# Generated by Django 3.1.3 on 2020-11-28 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0008_auto_20201121_2027'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cerificate',
            new_name='Certificate',
        ),
        migrations.RenameModel(
            old_name='CerificateType',
            new_name='CertificateType',
        ),
    ]
