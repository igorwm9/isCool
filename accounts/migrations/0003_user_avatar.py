# Generated by Django 2.0.1 on 2018-01-23 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180122_0152'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank='true', null='true', upload_to='avatars', verbose_name='Avatar'),
        ),
    ]
