# Generated by Django 3.2.8 on 2021-10-09 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(path='/static/portfolio/images'),
        ),
    ]
