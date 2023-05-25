from random import choices

from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)
from django.urls import reverse

from .models import (
    ChineseCharacter,
    CharacterKey,
    RussianWord,
    EnglishWord
)
from .forms import ChineseCharacterForm
from utils.trial import create_character_from_file

RUBBISH = {
    ',': ' ', '.': ' ', '\\': ' ', '/': ' ', '(': ' ',
    ')': ' ', '}': ' ', '{': ' ', '`': ' ', '~': ' ',
    '[': ' ', ']': ' ', '*': ' '
}

bkrs_file = 'E:/Maks/Documents/Питон/Проекты/dabkrs_230205.txt'

create_character_from_file(
        bkrs_file,
        ChineseCharacter,
        RussianWord,
        EnglishWord,
        start_line=4
    )


def index(request):
    template_name = 'search_words/index.html'
    keys_list = CharacterKey.objects.all()
    try:
        ten_random_characters = set(
            choices(ChineseCharacter.objects.all(), k=10)
        )
    except IndexError:
        ten_random_characters = []
    context = {
        'keys_list': keys_list,
        'ten_random_characters': ten_random_characters
    }
    return render(request, template_name, context)


def search_result(request):
    template_name = 'search_words/search_result.html'
    search_raw = request.GET['input'].strip()
    table = search_raw.maketrans(RUBBISH)
    search = search_raw.translate(table).split()
    if search == []:
        return redirect('search_words:index')
    result_chinese = []
    result_pinyin = []
    result_russian = []
    for i in range(len(search)):
        # Проверяем, есть ли в запросе иероглифы
        result_chinese += ChineseCharacter.objects.filter(
            character__icontains=search[i]
        )
        # Проверяем, есть ли в запросе pinyin
        result_pinyin += ChineseCharacter.objects.filter(
            pinyin__icontains=search[i]
        )
        # Проверяем, есть ли в запросе русское слово
        result_russian += RussianWord.objects.filter(
            word__icontains=search[i]
        )
    context = {
        'result_chinese': result_chinese,
        'result_pinyin': result_pinyin,
        'result_russian': result_russian,
        'search': search,
    }
    return render(request, template_name, context)


def character_page(request, character):
    template_name = 'search_words/character_page.html'
    get_character = get_object_or_404(ChineseCharacter, character=character)
    characters_number = len(character)
    words_with_character = ChineseCharacter.objects.filter(
        character__icontains=character
        ).exclude(character=character)
    russian_words = get_character.russian_meaning.all()
    usage_examples = get_character.usage_examples.all()
    context = {
        'character': get_character,
        'characters_number': characters_number,
        'words_with_character': words_with_character,
        'russian_words': russian_words,
        'usage_examples': usage_examples
    }
    return render(request, template_name, context)


def character_create(request):
    template_name = 'search_words/character_create.html'
    if request.method == 'POST':
        form = ChineseCharacterForm(request.POST or None)
        if form.is_valid():
            form.save()
            character = form.cleaned_data['character']
            return redirect('search_words:character_page', character)
        context = {'form': form}
        return render(request, template_name, context)
    form = ChineseCharacterForm()
    context = {'form': form}
    return render(request, template_name, context)


def character_edit(request, character):
    pass
