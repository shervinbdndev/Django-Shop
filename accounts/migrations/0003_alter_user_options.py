# Generated by Django 4.0.2 on 2022-03-01 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_user_mobile_user_avatar_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
    ]
