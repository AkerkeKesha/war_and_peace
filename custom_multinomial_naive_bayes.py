import numpy as np
from typing import List, Dict, Tuple

SYMBOLS = '''0123456789!()-[]{};:'"\,<>./?@#$%^&*_~'''


class CustomMNB:

    def __init__(self):
        self.vocabulary = []
        self.prior_a, self.prior_b = 0, 0
        self.words_a, self.words_b = 0, 0
        self.total = self.words_a + self.words_b
        self.word_probs = []
        self.factor = 0.1

    def _tokenize(self, sentence: str) -> List[str]:
        tokens = ""
        for char in sentence.lower():
            if char not in SYMBOLS:
                tokens += char
        return tokens.split()

    def count_words(self, X: List[str], y: int) -> Dict[str, List[int]]:
        """

        :param X: document
        :param y: label
        :return: dict with key word: [A_count, B_count], counts[word][0] := class A
        """
        counts = {}
        for doc, label in zip(X, y):
            for word in self._tokenize(doc):
                # avoid KeyError
                if word not in counts:
                    counts[word] = [0, 0]
                counts[word][label] += 1
        return counts

    def prior_probas(self, counts: Dict[str, List[int]]) -> Tuple[float, float]:
        words_a, words_b = 0, 0
        for word, val in counts.items():
            words_a += val[0]
            words_b += val[1]
        self.total = words_a + words_b
        prior_a = words_a / self.total
        prior_b = words_b / self.total
        self.words_a = words_a
        self.words_b = words_b
        return prior_a, prior_b

    def word_probas(self, counts: Dict[str, List[int]]) -> List[Tuple[str, float, float]]:
        """
        for each word we calculate p(w|A) and p(w|B)
        :param counts:
        :return:
        """
        word_probas = []
        # self.vocabulary = [word for word, (class_a, class_b) in counts.items()]
        for word, val in counts.items():
            pw_a = val[0] / self.words_a
            pw_b = val[1] / self.words_b
            word_probas.append((word, pw_a, pw_b))
        return word_probas

    def fit(self, Xtrain: List[str], ytrain: List[int]) -> None:
        counts = self.count_words(Xtrain, ytrain)
        self.prior_a, self.prior_b = self.prior_probas(counts)
        self.word_probs = self.word_probas(counts)

    def predict(self, Xtest: List[str]) -> List[int]:
        y_pred = []
        for doc in Xtest:
            log_prob_a = log_prob_b = 0.0
            tokens = self._tokenize(doc)
            for word, pw_a, pw_b in self.word_probas:
                if word in tokens:
                    log_prob_a += np.exp(pw_a)
                    log_prob_b += np.exp(pw_b)
            pred_a = self.prior_b * np.exp(log_prob_a)
            pred_b = self.prior_b * np.exp(log_prob_b)

            if pred_a >= pred_b:
                y_pred.append(0)  # class A = label 0
            else:
                y_pred.append(1)
        return y_pred


