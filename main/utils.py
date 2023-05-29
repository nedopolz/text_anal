import pymorphy3
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from main.config import KEY_WORDS, STOP_TAGS


def analyse_text(text: str):
    morph = pymorphy3.MorphAnalyzer()

    clear_text = re.sub(r'[^А-Яа-яЁё\s\-]', ' ', text)

    words = [word.lower() for word in clear_text.split()]

    normalized_words = []
    for word in words:
        word_info = morph.parse(word)[0]
        if len([stop_tag for stop_tag in STOP_TAGS if stop_tag in word_info.tag]) == 0 and word not in ['-']:
            word_info = morph.parse(word)[0]
            normalized_words.append(word_info.normal_form)

    unique_normalized_words = list(set(normalized_words))

    cosine_indexes = {}

    for topic, k_words in KEY_WORDS.items():
        count_vectorizer = CountVectorizer()
        vector_matrix = count_vectorizer.fit_transform([' '.join(unique_normalized_words), ' '.join(k_words)])
        cosine_similarity_matrix = cosine_similarity(vector_matrix)
        cosine_indexes[topic] = cosine_similarity_matrix[0][1]

    return {k: round(v, 4) for k, v in sorted(cosine_indexes.items(), key=lambda x: x[1], reverse=True)}
