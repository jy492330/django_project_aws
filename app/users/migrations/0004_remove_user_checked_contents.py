# Generated by Django 3.1.1 on 2022-08-25 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='checked_contents',
        ),
    ]
