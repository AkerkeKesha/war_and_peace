import re
from collections import Counter
from scipy.sparse import csr_matrix


class CustomCV:

    def cv_fit(self, data) -> int:
        """return index for given text"""
        unique_words = set()
        for sentence in data:
            for word in sentence.split(" "):
                word = re.sub(r'[!@#$(),\n"%^*?\:.;~`0-9]', '', word)
                if len(word) >= 2:
                    unique_words.add(word)
        vocab = {}
        for index, word in enumerate(sorted(list(unique_words))):
            vocab[word] = index
        return vocab

    def cv_fit_transform(self, data):
        vocabulary = self.cv_fit(data)
        row, col, val = [],[],[]
        for sentence_id, sentence in enumerate(data):
            count_word = dict(Counter(sentence.split(" ")))
            for word, count in count_word.items():
                word = re.sub(r'[!@#$(),\n"%^*?\:.;~`0-9]', '', word)
                if len(word) >= 2:
                    col_index = vocabulary[word]
                    row.append(sentence_id)
                    col.append(col_index)
                    val.append(count)
        return csr_matrix((val, (row, col)), shape=(len(data), len(vocabulary)))
