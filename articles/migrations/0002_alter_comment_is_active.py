# Generated by Django 3.2.5 on 2021-07-22 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
