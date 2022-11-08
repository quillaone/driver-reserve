# Generated by Django 4.1.3 on 2022-11-06 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_date', models.DateField()),
                ('collection_time', models.TimeField()),
            ],
            options={
                'db_table': 'shedule',
            },
        ),
    ]
