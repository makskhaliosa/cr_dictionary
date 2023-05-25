from django.db import models

NUMBER_OF_CHARACTERS = 20

PARTS_OF_SPEECH = [
    ('ГЛ.', 'глагол'),
    ('СУЩ.', 'существительное'),
    ('ПРИЛ.', 'прилагательное'),
    ('МЕСТ.', 'местоимение'),
    ('НАР.', 'наречие'),
    ('ПРИЧ.', 'причастие'),
    ('ДЕЕПРИЧ.', 'деепричастие'),
]


class RussianExample(models.Model):
    russian_text = models.TextField(
        max_length=500,
        verbose_name='Текст русского примера',
        help_text='Приведи пример на русском'
    )

    class Meta:
        ordering = ['russian_text']
        verbose_name = 'Пример на русском',
        verbose_name_plural = 'Примеры на русском'

    def __str__(self):
        return self.russian_text


class EnglishExample(models.Model):
    english_text = models.TextField(
        max_length=500,
        verbose_name='Текст английского примера',
        help_text='Приведи пример на английском'
    )

    class Meta:
        ordering = ['english_text']
        verbose_name = 'Пример на английском',
        verbose_name_plural = 'Примеры на английском'

    def __str__(self):
        return self.english_text


class ChineseExample(models.Model):
    chinese_text = models.TextField(
        max_length=500,
        verbose_name='Текст китайского примера',
        help_text='Приведи пример на китайском'
    )

    class Meta:
        verbose_name = 'Пример на китайском',
        verbose_name_plural = 'Примеры на китайском'

    def __str__(self):
        return self.chinese_text[:NUMBER_OF_CHARACTERS]


class ExamplePair(models.Model):
    russian_example = models.ForeignKey(
        RussianExample,
        on_delete=models.CASCADE,
        blank=True,
        related_name='example_pairs',
        verbose_name='Перевод на русском',
        help_text='Дай перевод на русском'
    )
    chinese_example = models.ForeignKey(
        ChineseExample,
        on_delete=models.CASCADE,
        blank=True,
        related_name='example_pairs',
        verbose_name='Перевод на китайском',
        help_text='Дай перевод на китайском'
    )
    english_example = models.ForeignKey(
        EnglishExample,
        on_delete=models.CASCADE,
        blank=True,
        default=1,
        related_name='example_pairs',
        verbose_name='Перевод на английском',
        help_text='Дай перевод на английском'
    )

    class Meta:
        verbose_name = 'Пример употреблений'
        verbose_name_plural = 'Примеры употреблений'

    def __str__(self):
        return self.chinese_example.chinese_text


class RussianWord(models.Model):
    word = models.CharField(
        max_length=255,
        verbose_name='Слово',
        help_text='Введи русское слово',
        unique=True
    )
    part_of_speech = models.CharField(
        max_length=20,
        choices=PARTS_OF_SPEECH,
        default='Пусто'
    )
    usage_examples = models.ManyToManyField(
        RussianExample,
        related_name='russian_words',
        verbose_name='Примеры употребления',
        help_text='Примеры употребления на русском',
        blank=True
    )

    class Meta:
        ordering = ['word']
        verbose_name = 'Русское слово'
        verbose_name_plural = 'Русские слова'

    def __str__(self):
        return self.word


class EnglishWord(models.Model):
    word = models.CharField(
        max_length=255,
        verbose_name='Английское слово',
        help_text='Введи английское слово',
        unique=True
    )
    part_of_speech = models.CharField(
        max_length=20,
        choices=PARTS_OF_SPEECH,
        default=0
    )
    usage_examples = models.ManyToManyField(
        EnglishExample,
        related_name='english_words',
        verbose_name='Примеры употребления',
        help_text='Примеры употребления на английском',
        blank=True
    )

    class Meta:
        ordering = ['word']
        verbose_name = 'Английское слово'
        verbose_name_plural = 'Английские слова'

    def __str__(self):
        return self.word


class CharacterKey(models.Model):
    key = models.CharField(
        max_length=10,
        verbose_name='Ключ',
        help_text='Введи китайский ключ'
    )
    pinyin = models.CharField(max_length=50)
    russian_meaning = models.ManyToManyField(
        RussianWord,
        related_name='character_keys',
        verbose_name='Русское значение',
        help_text='Напиши русский первод',
        blank=True,
        editable=True
    )

    class Meta:
        ordering = ['pinyin']
        verbose_name = 'Ключ'
        verbose_name_plural = 'Ключи'

    def __str__(self):
        return self.key


class ChineseCharacter(models.Model):
    character = models.CharField(
        max_length=20,
        verbose_name='Китайское слово',
        help_text='Введи слово на китайском'
    )
    pinyin = models.CharField(max_length=100)
    russian_meaning = models.ManyToManyField(
        RussianWord,
        related_name='characters',
        verbose_name='Русское значение',
        help_text='Дай русский перевод слова',
        blank=True,
        editable=True
    )
    english_meaning = models.ManyToManyField(
        EnglishWord,
        related_name='characters',
        verbose_name='Английское значение',
        help_text='Дай английский перевод слова',
        blank=True,
        editable=True
    )
    part_of_speech = models.CharField(
        max_length=20,
        choices=PARTS_OF_SPEECH,
        default='Пусто'
    )
    character_keys = models.ManyToManyField(
        CharacterKey,
        related_name='characters',
        verbose_name='Ключи',
        help_text='Укажи состав ключей иероглифа',
        blank=True,
        editable=True
    )
    usage_examples = models.ManyToManyField(
        ExamplePair,
        related_name='characters',
        verbose_name='Примеры употребления иероглифа',
        help_text='Приведи примеры с этим иероглифом',
        blank=True
    )

    class Meta:
        ordering = ['pinyin']
        verbose_name = 'Иероглиф'
        verbose_name_plural = 'Иероглифы'

    def __str__(self):
        return self.character
