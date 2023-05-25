# Generated by Django 4.1.2 on 2023-01-18 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search_words', '0010_alter_chineseexample_russian_translation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chineseexample',
            name='russian_translation',
        ),
        migrations.RemoveField(
            model_name='russianexample',
            name='chinese_translation',
        ),
        migrations.CreateModel(
            name='ExamplePair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chinese_example', models.ForeignKey(default='Пусто', help_text='Дай перевод на китайском', on_delete=django.db.models.deletion.CASCADE, related_name='chinese_examples', to='search_words.chineseexample', verbose_name='Перевод на китайском')),
                ('russian_example', models.ForeignKey(default='Пусто', help_text='Дай перевод на русском', on_delete=django.db.models.deletion.CASCADE, related_name='russian_examples', to='search_words.russianexample', verbose_name='Перевод на русском')),
            ],
            options={
                'verbose_name': 'Пример употреблений',
                'verbose_name_plural': 'Примеры употреблений',
            },
        ),
    ]
