# Generated by Django 4.2.6 on 2023-10-10 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='parent_item',
        ),
    ]
