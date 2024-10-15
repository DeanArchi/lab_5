import re


def custom_sort_key(word):
    alphabet_ua = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    alphabet_en = 'abcdefghijklmnopqrstuvwxyz'

    word_lower = word.lower()

    if re.match(f"^[{alphabet_ua}]+$", word_lower):
        return 0, word_lower

    if re.match(f"^[{alphabet_en}]+$", word_lower):
        return 1, word_lower

    return 2, word_lower


def read_first_sentence(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()

            first_sentence = re.split(r'[.!?]', text)[0]

            print("Перше речення:")
            print(first_sentence)

            words = re.findall(r'\b\w+\b', first_sentence)
            print("\nСлова у реченні:")
            print(words)

            words.sort(key=custom_sort_key)
            print("\nВідсортовані слова:")
            print(words)

            print("\nКількість слів:", len(words))
    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")


# Виклик функції
filename = 'text.txt'
read_first_sentence(filename)
