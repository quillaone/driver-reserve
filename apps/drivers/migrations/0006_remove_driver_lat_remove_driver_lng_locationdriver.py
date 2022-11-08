# Generated by Django 4.1.3 on 2022-11-08 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0005_alter_driver_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='lng',
        ),
        migrations.CreateModel(
            name='LocationDriver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, default='Colombia', max_length=100, null=True)),
                ('lat', models.FloatField(default=0)),
                ('lng', models.FloatField(default=0)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='drivers.driver')),
            ],
            options={
                'db_table': 'location_drivers',
            },
        ),
    ]
