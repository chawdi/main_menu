# Generated by Django 4.2.6 on 2023-10-26 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='menu_name',
            field=models.CharField(default='default_menu', max_length=100),
        ),
    ]
