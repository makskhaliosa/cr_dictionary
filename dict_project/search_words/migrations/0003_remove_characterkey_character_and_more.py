# Generated by Django 4.1.2 on 2022-10-12 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_words', '0002_rename_characterkeys_characterkey'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='characterkey',
            name='character',
        ),
        migrations.RemoveField(
            model_name='russianword',
            name='character',
        ),
    ]
