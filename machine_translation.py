from deep_translator import GoogleTranslator
from utils import get_clean_file
from transformers import MarianMTModel, MarianTokenizer
from typing import List

MODEL_RU_EN = 'Helsinki-NLP/opus-mt-ru-en'
TOKENIZER = MarianTokenizer.from_pretrained(MODEL_RU_EN)
MODEL = MarianMTModel.from_pretrained(MODEL_RU_EN)


def translate_from(file: str, src_languaguge: str, tgt_language: str) -> str:
    translated = GoogleTranslator(source=src_languaguge, target=tgt_language).translate_file(file)
    return translated


def marian_translate(texts: List[str], model=MODEL, tokenizer=TOKENIZER) -> str:
    translated = model.generate(**tokenizer(texts, return_tensors="pt", padding=True))
    return "\n".join([tokenizer.decode(t, skip_special_tokens=True) for t in translated])


if __name__ == '__main__':
    test = marian_translate(texts=[
        "Разве можно, имея чувство, оставаться спокойною в наше время? — сказала Анна Павловна.",
        "— Вы весь вечер у меня, надеюсь?",
        "— А праздник английского посланника?",
        "Нынче середа."], model=MODEL, tokenizer=TOKENIZER)
    print(test)


