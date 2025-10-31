# Описание проекта
Проект демонстрирует модуль tokenizer.py, который реализует токенизацию текста тремя способами и может использоваться как подгружаемая библиотека. 

Способы токенизации: 
Простая токенизация — с использованием регулярных выражений;
NLTK токенизация — с использованием библиотеки NLT(word_tokenize);
spaCy токенизация — с использованием библиотеки spaCy. 

# Инструкции по установке
1. Создайте виртуальное окружение. Для этого введите в терминал: 

python -m venv tokenizer_env
source tokenizer_env/bin/activate

2. Установите зависимости: 

pip install -r requirements.txt

3. Скачайте модели для spaCy:

python3 -m spacy download en_core_web_sm

# Примеры использования
Пример использования через demo.py:

python demo.py

Пример для импорта модуля:

from tokenizer import TextTokenizer

def main():
    tokenizer = TextTokenizer()

    # Пример текста для токенизации
    sample_text = "Hello, world! This is a test sentence. How are you today?"

    # Применяем все методы токенизации
    results = tokenizer.tokenize_all(sample_text)

    # Выводим результаты
    for method, tokens in results.items():
        print(f"{method}: {tokens}")

if __name__ == "__main__":
    main()

# Описание методов
simple_tokenize(text) — простая токенизация с использованием регулярных выражений.
nltk_tokenize(text) — токенизация с использованием NLTK.
spacy_tokenize(text) — токенизация с использованием spaCy.
tokenize_all(text) — применяет все три метода и возвращает словарь с результатами.