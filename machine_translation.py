from typing import List
import torch
import math
from transformers import MarianMTModel, MarianTokenizer

if torch.cuda.is_available():
  dev = "cuda"
else:
  dev = "cpu"
DEVICE = torch.device(dev)

MODEL_RU_EN = 'Helsinki-NLP/opus-mt-ru-en'
TOKENIZER = MarianTokenizer.from_pretrained(MODEL_RU_EN)
MODEL = MarianMTModel.from_pretrained(MODEL_RU_EN).to(DEVICE)
BATCH_SIZE = 24


def marian_translate(texts: List[str], model=MODEL, tokenizer=TOKENIZER, device=DEVICE) -> List[str]:
    batches = math.ceil(len(texts) / BATCH_SIZE)
    translated = []
    for i in range(batches):
        sentence_batch = texts[i * BATCH_SIZE:(i + 1) * BATCH_SIZE]
        translated_batch = model.generate(**tokenizer(sentence_batch, return_tensors="pt", padding=True).to(device)).to(
            device)
        translated += translated_batch
    translated_sentences = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]
    return translated_sentences


if __name__ == '__main__':
    test = marian_translate(texts=[
        "Разве можно, имея чувство, оставаться спокойною в наше время? — сказала Анна Павловна.",
        "— Вы весь вечер у меня, надеюсь?",
        "— А праздник английского посланника?",
        "Нынче середа."], model=MODEL, tokenizer=TOKENIZER)
    print(test)
    with open("./data/passage_enemy.txt") as fh:
        sample = fh.read()
    tolstoy_translated = marian_translate(sample)
    for sentence in tolstoy_translated:
        with open('./data/translated_passage_enemy.txt', 'a') as fh:
            fh.write(f"{sentence}\n")
    print("done translating")





