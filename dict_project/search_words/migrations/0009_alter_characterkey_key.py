# Generated by Django 4.1.2 on 2023-01-18 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_words', '0008_chineseexample_alter_characterkey_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characterkey',
            name='key',
            field=models.CharField(help_text='Введи китайский ключ', max_length=10, verbose_name='Ключ'),
        ),
    ]