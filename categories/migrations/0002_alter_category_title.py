# Generated by Django 3.2.5 on 2021-07-15 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
