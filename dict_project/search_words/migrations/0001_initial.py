# Generated by Django 4.1.2 on 2022-10-10 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChineseCharacter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.CharField(max_length=20)),
                ('pinyin', models.CharField(max_length=50)),
                ('russian_meaning', models.CharField(max_length=100)),
                ('characters_number', models.IntegerField()),
                ('keys_set', models.CharField(max_length=50)),
                ('usage_examples', models.CharField(max_length=400)),
                ('lines_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RussianWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50)),
                ('first_letter', models.CharField(max_length=1)),
                ('letters_number', models.IntegerField(default=0)),
                ('chinese_meaning', models.CharField(max_length=20)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search_words.chinesecharacter')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterKeys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=10)),
                ('pinyin', models.CharField(max_length=20)),
                ('russian_meaning', models.CharField(max_length=50)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search_words.chinesecharacter')),
            ],
        ),
    ]
