# Generated by Django 3.2.7 on 2021-10-02 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20210912_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
