# Generated by Django 3.2.7 on 2021-09-12 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='urls',
            new_name='url',
        ),
        migrations.AddField(
            model_name='project',
            name='is_visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='project',
            name='rank',
            field=models.IntegerField(default=0),
        ),
    ]