# Generated by Django 4.0.3 on 2022-03-27 02:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0005_article_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
    ]
