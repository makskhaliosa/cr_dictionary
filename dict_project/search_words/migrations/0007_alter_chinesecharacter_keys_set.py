# Generated by Django 4.1.2 on 2023-01-15 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_words', '0006_alter_chinesecharacter_keys_set_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chinesecharacter',
            name='keys_set',
            field=models.ManyToManyField(blank=True, related_name='characters', to='search_words.characterkey'),
        ),
    ]
