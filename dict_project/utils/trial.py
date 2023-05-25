from io import StringIO
import csv


from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

from search_words.models import (
    ChineseCharacter,
    RussianWord,
    EnglishWord
)

filename = 'E:\Maks\Documents\Питон\Проекты\kljuchi\Ключи китайских иероглифов.pdf'
def parser():
    output_string = StringIO()
    with open(filename, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)

    print(output_string.getvalue())

russian_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫБЭЮЯ'



other_list4 = []
"""Функция для извлечения текста из пдф с помощью модуля pdfminer

>>> from pdfminer.high_level import extract_text
>>> text = extract_text('samples/simple1.pdf')
>>> print(repr(text))
'Hello \n\nWorld\n\nHello \n\nWorld\n\nH e l l o  \n\nW o r l d\n\nH e l l o  \n\nW o r l d\n\n\x0c'
>>> print(text)

Код для извлечения чистого списка без лишних символов
for x in list4:
    if len(x) == 1:
        other_list4.append(x)
    elif len(x) == 2:
        for y in other_list4:
            if x in y:
                continue
            else:
                cr_dictionary1[x[0]] = {'pinyin': x[1], 'russian_meaning': ''}
    elif len(x) == 3:
        if x[0][0] in russian_alphabet:
            cr_dictionary1[x[1]] = {'pinyin': x[2], 'russian_meaning': x[0]}
        else:
            for y in other_list4:
                if x in y:
                    continue
                else:
                    cr_dictionary1[x[0]] = {'pinyin': f'{x[1]}{x[2]}', 'russian_meaning': ''}
    elif len(x) == 4:
        cr_dictionary1[x[1]] = {'pinyin': x[2] + x[3], 'russian_meaning': x[0]}
    else:
        continue
        

load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/ru_ch.csv'
into table search_words_chinesecharacter
(character, pinyin, russian_meaning, characters_number, @dummy, keys_set, @dummy, usage_examples, @dummy, lines_number, @dummy)
fields terminated by ','
lines terminated by '\r\n'
ignore 1 lines

"""
new_file = 'E:/Maks/Documents/Питон/Проекты/ru_ch.csv'
other_name = 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/ru_ch.csv'
fieldnames = ['character', 'pinyin', 'russian_meaning', 'characters_number', 'keys_set', 'usage_examples', 'lines_number']
'E:/Maks/Documents/Питон/Проекты/kljuchi/keys.txt'


def characters_into_csv(filename, dict_name, fieldnames):
    """функция для записи словаря в csv файл с адресом filename"""
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=fieldnames,
            restval='NULL',
            extrasaction='ignore'
        )
        writer.writeheader()
        for key, value in dict_name.items():
            writer.writerow({
                'character': key,
                'pinyin': value['pinyin'],
                'russian_meaning': value['russian_meaning']
            })

"""
d = {'he': {'name': 'Maks', 'fam': 'Lion'}}
for k, v in d.items():
    print(k, v['name'])
# and not
                #model_name1.objects.filter(character=lines[line_num]).exists()
            #):
from utils.trial import create_character_from_file
from search_words.models import ChineseCharacter, RussianWord, EnglishWord
bkrs_file = 'E:/Maks/Documents/Питон/Проекты/dabkrs_230205.txt'
"""
bkrs_file = 'E:/Maks/Documents/Питон/Проекты/dabkrs_230205.txt'


def create_character_from_file(
    filename,
    model_name1,
    model_name2=None,
    model_name3=None,
    start_line=1
):
    """Функция для чтения файла filename и создания иероглифа"""
    alphabet_rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alphabet_en = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_pinyin = 'āǎáàēèéěíīǐìōóòǒùūǔú'
    rubbish = {
        '[': '', 'm': '', '1': '', ']': '', 'p': '', '/': '', 'i': '',
        'c': '', 'r': '', 'e': '', 'f': '', '2': '', '*': '', 'x': ''
    }
    with open(filename, 'r', encoding='utf-8', newline='\n') as f:
        lines = f.readlines()
        for line_num in range(start_line, len(lines), 4):
            if (lines[line_num]):
                table = lines[line_num+2].maketrans(rubbish)
                clean_line = lines[line_num+2].translate(table)
                if clean_line[1].lower() in alphabet_rus:
                    model_name2.objects.get_or_create(
                        word=clean_line[:255]
                    )
                    rus_word = model_name2.objects.get(word=clean_line[:255])
                    print(rus_word)
                    model_name1.objects.get_or_create(
                        character=lines[line_num],
                        pinyin=lines[line_num + 1]
                    )
                    char = model_name1.objects.get(character=lines[line_num])
                    rus_word.characters.add(char)
                elif clean_line[1].lower() in alphabet_en:
                    model_name3.objects.get_or_create(
                        word=clean_line[:255]
                    )
                    en_word = model_name3.objects.get(word=clean_line[:255])
                    print(en_word)
                    model_name1.objects.get_or_create(
                        character=lines[line_num],
                        pinyin=lines[line_num + 1]
                    )
                    char = model_name1.objects.get(character=lines[line_num])
                    en_word.characters.add(char)


if __name__ == '__main__':
    create_character_from_file(
        bkrs_file,
        ChineseCharacter,
        RussianWord,
        EnglishWord,
        start_line=5
    )