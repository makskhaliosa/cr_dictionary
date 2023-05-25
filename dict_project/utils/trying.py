from pdfminer.high_level import extract_text

nums = '1234567890'
alphabet = 'abcdefghijklmnopqrstuvwxyzǔèéùéìāǐāǔéěóāīāíīìǎīǔīáīō.,?!–òìàǒǐǚéīǐ;ùèǐǎōēūú()ē'
alphabet_rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

file_name = 'E:\Maks\Documents\Питон\Проекты\kljuchi\Ключи китайских иероглифов.pdf'

text = extract_text(file_name)

file_txt = 'E:\Maks\Documents\Питон\Проекты\kljuchi\keys.txt'


def create_key(filename, model_name):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            a = model_name()
            a.key = line
            a.save()
