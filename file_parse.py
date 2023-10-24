import os
import re


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def position_of_first_word(text):
    words = text.split()
    most_common = max(set(words), key=words.count)

    for index, word in enumerate(words):
        if word == most_common:
            return index + 1
    return None


def repeat_word(text):
    return max(set(text), key=text.count)


def process_files(directory_path):
    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        print("Указанная директория не существует или не является папкой.")
        return None

    result = {}
    for filename in os.listdir(directory_path):
        file = os.path.join(directory_path, filename)
        if os.path.isfile(file):
            with open(file, 'r', encoding='utf-8') as file:
                data = file.read()
                name, expansion = os.path.splitext(filename)
                count_line = len(data.split('\n'))
                clear_data = data.split()
                word_clear = re.sub(r'[^\w\s]', ' ', data)
                word = len(word_clear.split())
                repeat = repeat_word(clear_data)
                first_on_in_text = position_of_first_word(data)
                result[filename] = {
                    "Название файла": name,
                    "Расширение файла": expansion,
                    "Количество строк": count_line,
                    "Количество слов": word,
                    "Часто встречающееся слово": repeat,
                    "Первое включение в текст": first_on_in_text,
                    "Содержимое": data
                }
    return result


def write_file(filename, content):
    sorted_content = dict(sorted(content.items()))

    with open(filename, 'w', encoding='utf-8') as file:
        for file_data in sorted_content.values():
            for key, value in file_data.items():
                file.write("{}: {}\n".format(key, value))
            file.write("\n")
    print('Данные получены и обработаны!')
