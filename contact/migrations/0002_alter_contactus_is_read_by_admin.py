# Generated by Django 4.0.2 on 2022-02-20 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='is_read_by_admin',
            field=models.BooleanField(default=False, verbose_name='read by admin'),
        ),
    ]
