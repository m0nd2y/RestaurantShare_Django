# Generated by Django 3.2.5 on 2021-08-04 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShareRes', '0002_restaurant'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='restaurant_line',
            new_name='restaurant_link',
        ),
    ]