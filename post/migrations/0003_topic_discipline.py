# Generated by Django 2.0.1 on 2018-01-21 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discipline', '0003_discipline_teacher'),
        ('post', '0002_auto_20180118_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='discipline',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='discipline.Discipline', verbose_name='Disciplina'),
            preserve_default=False,
        ),
    ]
