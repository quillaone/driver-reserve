# Generated by Django 4.1.3 on 2022-11-06 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='locationdriver',
            old_name='latitude',
            new_name='lat',
        ),
        migrations.RenameField(
            model_name='locationdriver',
            old_name='longitude',
            new_name='lgn',
        ),
    ]