# Generated by Django 3.1.1 on 2022-08-25 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
    ]
