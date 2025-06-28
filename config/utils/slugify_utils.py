import re
import unicodedata


class UkrSlugify:
    def __init__(self):
        self.translit_map = {
            'А': 'A',
            'а': 'a',
            'Б': 'B',
            'б': 'b',
            'В': 'V',
            'в': 'v',
            'Г': 'H',
            'г': 'h',
            'Ґ': 'G',
            'ґ': 'g',
            'Д': 'D',
            'д': 'd',
            'Е': 'E',
            'е': 'e',
            'Є': 'Ye',
            'є': 'ie',
            'Ж': 'Zh',
            'ж': 'zh',
            'З': 'Z',
            'з': 'z',
            'И': 'Y',
            'и': 'y',
            'І': 'I',
            'і': 'i',
            'Ї': 'Yi',
            'ї': 'i',
            'Й': 'Y',
            'й': 'i',
            'К': 'K',
            'к': 'k',
            'Л': 'L',
            'л': 'l',
            'М': 'M',
            'м': 'm',
            'Н': 'N',
            'н': 'n',
            'О': 'O',
            'о': 'o',
            'П': 'P',
            'п': 'p',
            'Р': 'R',
            'р': 'r',
            'С': 'S',
            'с': 's',
            'Т': 'T',
            'т': 't',
            'У': 'U',
            'у': 'u',
            'Ф': 'F',
            'ф': 'f',
            'Х': 'Kh',
            'х': 'kh',
            'Ц': 'Ts',
            'ц': 'ts',
            'Ч': 'Ch',
            'ч': 'ch',
            'Ш': 'Sh',
            'ш': 'sh',
            'Щ': 'Shch',
            'щ': 'shch',
            'Ю': 'Yu',
            'ю': 'iu',
            'Я': 'Ya',
            'я': 'ia',
            'Ь': '',
            'ь': '',
            "'": '',
            '’': '',
            'ʼ': '',
        }

    def contains_cyrillic(self, text: str) -> bool:
        return bool(re.search(r'[а-яА-ЯёЁґҐєЄіІїЇ]', text))

    def transliterate(self, text: str) -> str:
        result = []
        for i, char in enumerate(text):
            if char in ['Є', 'є']:
                result.append('Ye' if i == 0 else 'ie')
            elif char in ['Ї', 'ї']:
                result.append('Yi' if i == 0 else 'i')
            elif char in ['Й', 'й']:
                result.append('Y' if i == 0 else 'i')
            elif char in ['Ю', 'ю']:
                result.append('Yu' if i == 0 else 'iu')
            elif char in ['Я', 'я']:
                result.append('Ya' if i == 0 else 'ia')
            else:
                result.append(self.translit_map.get(char, char))
        return ''.join(result)

    def strip_accents(self, text: str) -> str:
        return (
            unicodedata.normalize('NFKD', text)
            .encode('ascii', 'ignore')
            .decode('ascii')
        )

    def slugify(self, text: str) -> str:
        if self.contains_cyrillic(text):
            text = self.transliterate(text)
        else:
            text = self.strip_accents(text)

        text = text.lower()
        text = re.sub(r'[^\w\s-]', '', text)
        text = re.sub(r'[\s_-]+', '-', text)
        return text.strip('-')

    def __call__(self, text):
        return self.slugify(text)


class SlugTrimmer:
    def __init__(self, default_max_length: int = 50, separator: str = '-'):
        self.default_max_length = default_max_length
        self.separator = separator

    def trim(self, slug: str, max_length: int = None) -> str:
        max_length = max_length or self.default_max_length

        if len(slug) <= max_length:
            return slug

        trimmed = slug[:max_length]
        if self.separator not in trimmed:
            return trimmed.rstrip(self.separator)

        return trimmed[: trimmed.rfind(self.separator)].rstrip(self.separator)

    def __call__(self, slug: str, max_length: int = None) -> str:
        return self.trim(slug, max_length=max_length)


class SlugUnique:
    def __init__(self, model_cls=None, field_name='slug', separator='-', max_length=50):
        if model_cls is None:
            raise ValueError('model_cls must be provided')
        self.model_cls = model_cls
        self.field_name = field_name
        self.separator = separator
        self.max_length = max_length

    def __call__(self, base_slug):
        slug = base_slug
        counter = 1
        while self.model_cls.objects.filter(**{self.field_name: slug}).exists():
            suffix = f'{self.separator}{counter}'
            allowed = self.max_length - len(suffix)
            slug = f'{base_slug[:allowed].rstrip(self.separator)}{suffix}'
            counter += 1
        return slug


slugify = UkrSlugify()
slug_trim = SlugTrimmer()
