from django import forms

from .models import ChineseCharacter


class ChineseCharacterForm(forms.ModelForm):
    class Meta:
        model = ChineseCharacter
        fields = [
            'character',
            'pinyin',
            'russian_meaning',
            'character_keys',
            'usage_examples'
        ]
