from django.contrib import admin
from .models import (
    CharacterKey,
    ChineseCharacter,
    RussianWord,
    EnglishWord,
    ChineseExample,
    RussianExample,
    EnglishExample,
    ExamplePair
)


class CharacterKeyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'key', 'pinyin')
    search_fields = ('pinyin',)


class ChineseCharacterAdmin(admin.ModelAdmin):
    list_display = ('character', 'pinyin')
    search_field = ('character', 'russian_meaning', 'character_keys')


class ExamplePairAdmin(admin.ModelAdmin):
    list_display = ('pk', 'russian_example', 'chinese_example')


admin.site.register(ChineseCharacter, ChineseCharacterAdmin)
admin.site.register(CharacterKey, CharacterKeyAdmin)
admin.site.register(RussianWord)
admin.site.register(EnglishWord)
admin.site.register(ChineseExample)
admin.site.register(RussianExample)
admin.site.register(EnglishExample)
admin.site.register(ExamplePair, ExamplePairAdmin)
