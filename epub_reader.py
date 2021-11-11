from typing import List
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup


BLACKLIST = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head',
    'input',
    'script',
    'style',
    'h1',
    'h2',
    'h3',
    'h4',
    'h5',
    'sup',
]


def get_epub_chapters(epub_path: str) -> List[bytes]:
    book = epub.read_epub(epub_path)
    chapters = []
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            chapters.append(item.get_content())
    return chapters


def chap2text(chap: bytes) -> str:
    output = ''
    soup = BeautifulSoup(chap, 'html.parser')
    text = soup.find_all(text=True)
    for t in text:
        if t.parent.name not in BLACKLIST:
            output += '{} '.format(t)
    return output


def html2ttext(thtml: List[bytes]) -> List[str]:
    output = []
    for html in thtml:
        text = chap2text(html)
        output.append(text)
    return output


def epub2text(epub_path: str) -> List[str]:
    chapters = get_epub_chapters(epub_path)
    ttext = html2ttext(chapters)
    return ttext


