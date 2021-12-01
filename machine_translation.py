from deep_translator import GoogleTranslator
from utils import get_clean_file
from transformers import MarianMTModel, MarianTokenizer
from typing import List
import time

MODEL_RU_EN = 'Helsinki-NLP/opus-mt-ru-en'
TOKENIZER = MarianTokenizer.from_pretrained(MODEL_RU_EN)
MODEL = MarianMTModel.from_pretrained(MODEL_RU_EN)


def translate_from(file: str, src_languaguge: str, tgt_language: str) -> str:
    translated = GoogleTranslator(source=src_languaguge, target=tgt_language).translate_file(file)
    return translated


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
    # start_time = time.time()
    # clean_file_path = get_clean_file('test.txt')
    # with open(clean_file_path) as fh:
    #     tolstoy_texts = fh.readlines()
    # print(f"{len(tolstoy_texts)} sentences to feed")
    # tolstoy_translated = marian_translate(tolstoy_texts)
    # print(f"{len(tolstoy_translated)} sentences translated")
    # for sentence in tolstoy_translated:
    #     with open('./data/tolstoy_translated.txt', 'a') as fh:
    #         fh.write(f"{sentence}\n")
    # print(f"{time.time() - start_time} seconds to translate")
#     Process finished with exit code 137 (interrupted by signal 9: SIGKILL)


