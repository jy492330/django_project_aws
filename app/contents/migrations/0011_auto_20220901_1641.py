# Generated by Django 3.1.1 on 2022-09-01 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0010_auto_20220901_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostedcontent',
            name='folder_path',
            field=models.CharField(max_length=300),
        ),
    ]
