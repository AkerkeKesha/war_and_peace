from transformers import MarianMTModel, MarianTokenizer
from typing import List

MODEL_RU_EN = 'Helsinki-NLP/opus-mt-ru-en'
TOKENIZER = MarianTokenizer.from_pretrained(MODEL_RU_EN)
MODEL = MarianMTModel.from_pretrained(MODEL_RU_EN)


def marian_translate(texts: List[str], model=MODEL, tokenizer=TOKENIZER) -> List[str]:
    translated = model.generate(**tokenizer(texts, return_tensors="pt", padding=True))
    translated_sentences = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]
    return translated_sentences


if __name__ == '__main__':
    test = marian_translate(texts=[
        "Разве можно, имея чувство, оставаться спокойною в наше время? — сказала Анна Павловна.",
        "— Вы весь вечер у меня, надеюсь?",
        "— А праздник английского посланника?",
        "Нынче середа."], model=MODEL, tokenizer=TOKENIZER)
    print(test)



