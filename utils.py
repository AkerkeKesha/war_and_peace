import os
import spacy

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
nlp = spacy.load('ru_core_news_sm', disable=['ner'])
nlp.add_pipe("sentencizer")


def get_raw_file(dirname: str, filename: str) -> str:
    return os.path.join(ROOT_DIR, 'raw_data', dirname, filename)


def get_sample_file(filename: str) -> str:
    return os.path.join(ROOT_DIR, 'sample', filename)


def get_clean_file(filename: str) -> str:
    return os.path.join(ROOT_DIR, 'data', filename)


def chapter_sentencizer(chapter):
    doc = nlp(chapter)
    sentences = [str(sent).strip() for sent in doc.sents]
    text = '\n'.join(sentences)
    return text


def find_required_paragraph(chapter, start_text, end_text):
    '''
    Used for ground truth vs reference paragraph WER calculation
    :param chapter:
    :param start_text:
    :param end_text:
    :return:
    '''
    start_index = chapter.find(start_text)
    end_index = chapter.find(end_text)
    length = len(end_text)
    return chapter[start_index: end_index + length]
