# Generated by Django 3.2.5 on 2021-07-23 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210723_1119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='skills',
            new_name='experience',
        ),
    ]
