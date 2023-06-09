# Generated by Django 4.1.2 on 2022-11-24 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_words', '0005_alter_chinesecharacter_keys_set'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chinesecharacter',
            name='keys_set',
            field=models.ManyToManyField(blank=True, null=True, related_name='characters', to='search_words.characterkey'),
        ),
        migrations.AlterField(
            model_name='chinesecharacter',
            name='usage_examples',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
