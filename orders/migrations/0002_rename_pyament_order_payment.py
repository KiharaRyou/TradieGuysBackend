# Generated by Django 3.2.5 on 2021-07-18 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='pyament',
            new_name='payment',
        ),
    ]
