# Generated by Django 4.1.2 on 2023-02-05 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search_words', '0015_alter_chinesecharacter_usage_examples_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnglishExample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english_text', models.TextField(help_text='Приведи пример на английском', max_length=500, verbose_name='Текст английского примера')),
            ],
            options={
                'verbose_name': ('Пример на английском',),
                'verbose_name_plural': 'Примеры на английском',
                'ordering': ['english_text'],
            },
        ),
        migrations.AlterModelOptions(
            name='russianword',
            options={'ordering': ['word'], 'verbose_name': 'Русское слово', 'verbose_name_plural': 'Русские слова'},
        ),
        migrations.AlterField(
            model_name='chineseexample',
            name='chinese_text',
            field=models.TextField(help_text='Приведи пример на китайском', max_length=500, verbose_name='Текст китайского примера'),
        ),
        migrations.AlterField(
            model_name='examplepair',
            name='chinese_example',
            field=models.ForeignKey(blank=True, help_text='Дай перевод на китайском', on_delete=django.db.models.deletion.CASCADE, related_name='example_pairs', to='search_words.chineseexample', verbose_name='Перевод на китайском'),
        ),
        migrations.AlterField(
            model_name='examplepair',
            name='russian_example',
            field=models.ForeignKey(blank=True, help_text='Дай перевод на русском', on_delete=django.db.models.deletion.CASCADE, related_name='example_pairs', to='search_words.russianexample', verbose_name='Перевод на русском'),
        ),
        migrations.AlterField(
            model_name='russianword',
            name='word',
            field=models.CharField(help_text='Введи русское слово', max_length=255, unique=True, verbose_name='Слово'),
        ),
        migrations.CreateModel(
            name='EnglishWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(help_text='Введи английское слово', max_length=255, unique=True, verbose_name='Английское слово')),
                ('part_of_speech', models.CharField(choices=[('ГЛ.', 'глагол'), ('СУЩ.', 'существительное'), ('ПРИЛ.', 'прилагательное'), ('МЕСТ.', 'местоимение'), ('НАР.', 'наречие'), ('ПРИЧ.', 'причастие'), ('ДЕЕПРИЧ.', 'деепричастие')], default=0, max_length=20)),
                ('usage_examples', models.ManyToManyField(blank=True, help_text='Примеры употребления на английском', related_name='english_words', to='search_words.englishexample', verbose_name='Примеры употребления')),
            ],
            options={
                'verbose_name': 'Английское слово',
                'verbose_name_plural': 'Английские слова',
                'ordering': ['word'],
            },
        ),
        migrations.AddField(
            model_name='chinesecharacter',
            name='english_meaning',
            field=models.ManyToManyField(blank=True, help_text='Дай английский перевод слова', related_name='characters', to='search_words.englishword', verbose_name='Английское значение'),
        ),
    ]
