# Generated by Django 2.2.14 on 2020-11-10 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tuner',
            name='unc',
            field=models.CharField(blank=True, default=0, max_length=10, verbose_name='UNC'),
        ),
    ]
