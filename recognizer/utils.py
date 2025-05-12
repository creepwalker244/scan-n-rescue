import re

# Допустимые символы в госномерах (ГОСТ)
VALID_CHARS = 'АВЕКМНОРСТУХ'

def clean_and_validate(text: str) -> str:
    text = text.upper()
    text = text.replace(" ", "").replace("-", "")

    # Замена русских/англ символов визуально похожих
    replacements = {
        "A": "А", "B": "В", "E": "Е", "K": "К",
        "M": "М", "H": "Н", "O": "О", "P": "Р",
        "C": "С", "T": "Т", "Y": "У", "X": "Х"
    }
    text = ''.join([replacements.get(c, c) for c in text])

    # Валидация по шаблону
    pattern = r'^[' + VALID_CHARS + r']\d{3}[' + VALID_CHARS + r']{2}\d{2,3}$'
    if re.match(pattern, text):
        return text
    return ""
