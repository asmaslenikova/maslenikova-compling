"""
Модуль для токенизации текста различными способами
"""

import re

class TextTokenizer:
    def __init__(self):
        """Инициализация токенизатора: не изменяйте эту строчку кода"""
        pass

    def simple_tokenize(self, text):
        """
        Простая токенизация по пробелам и знакам препинания

        Args:
            text (str): Входной текст

        Returns:
            list: Список токенов
        """
        tokens = re.findall(r"\b\w+\b", text.lower())
        return tokens

    def nltk_tokenize(self, text):
        """
        Токенизация с использованием NLTK

        Args:
            text (str): Входной текст

        Returns:
            list: Список токенов или сообщение об ошибке
        """
        # Реализация NLTK токенизации
        try:
            import nltk
            from nltk.tokenize import word_tokenize
            nltk.download('punkt')
            return word_tokenize(text)
        except ImportError:
            return ["Ошибка: библиотека NLTK не установлена"]

    def spacy_tokenize(self, text):
        """
        Токенизация с использованием spaCy

        Args:
            text (str): Входной текст

        Returns:
            list: Список токенов или сообщение об ошибке
        """
        # Реализация spaCy токенизации
        try:
            import spacy
            nlp = spacy.load("en_core_web_sm")
            doc = nlp(text)
            return [token.text for token in doc]
        except ImportError:
            return ["Ошибка: библиотека spaCy не установлена"]
        except OSError:
            return ["Ошибка: отсутствует модель 'en_core_web_sm'"]

    def tokenize_all(self, text):
        """
        Применяет все доступные методы токенизации

        Args:
            text (str): Входной текст

        Returns:
            dict: Словарь с результатами всех методов
        """
        # Реализация вызова всех методов
        return {
            "simple": self.simple_tokenize(text),
            "nltk": self.nltk_tokenize(text),
            "spacy": self.spacy_tokenize(text)
            }

def demo():
    """Демонстрационная функция"""
    # Пример использования
    tokenizer = TextTokenizer()
    sample_text = "Hello, world! This is a test sentence. How are you today?"
    results = tokenizer.tokenize_all(sample_text)
    for method, tokens in results.items():
        print(f"\nМетод: {method}\nТокены: {tokens}")

if __name__ == "__main__":
    demo()