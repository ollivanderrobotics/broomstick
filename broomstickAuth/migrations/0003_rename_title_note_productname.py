# Generated by Django 3.2.9 on 2021-11-13 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('broomstickAuth', '0002_remove_note_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='title',
            new_name='productName',
        ),
    ]
