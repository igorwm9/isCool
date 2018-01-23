# Generated by Django 2.0.1 on 2018-01-23 11:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0004_topic_is_warning'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topic',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
            preserve_default=False,
        ),
    ]
