# Generated by Django 2.0.1 on 2018-01-23 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180123_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank='true', default='avatars/user.png', upload_to='avatars', verbose_name='Avatar'),
        ),
    ]