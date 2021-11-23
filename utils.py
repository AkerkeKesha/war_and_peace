import os
import re

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SENTENCE_PATTERN = r"[A-Z].*?[\.!?]"


def get_raw_file(dirname: str, filename: str) -> str:
    return os.path.join(ROOT_DIR, 'raw_data', dirname, filename)


def get_sample_file(filename: str) -> str:
    return os.path.join(ROOT_DIR, 'sample', filename)


def get_clean_file(filename: str) -> str:
    return os.path.join(ROOT_DIR, 'data', filename)


def make_sentence_per_line(s: str) -> str:
    for match in re.findall(SENTENCE_PATTERN, s):
        s = re.sub(match, f'{match}\n', s)
    return s
