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


def process_files(directory_path):
    files = [f for f in os.listdir(directory_path) if os.path.isfile(
        os.path.join(directory_path, f))]

    result = {}
    for file in files:
        file_path = os.path.join(directory_path, file)
        data = read_file(file_path)
        name, expansion = os.path.splitext(file)
        count_line = len(data.split('\n'))
        clear_data = data.split()
        word_clear = re.sub(r'[^\w\s]', ' ', data)
        word = len(word_clear.split())
        repeat = max(set(clear_data), key=clear_data.count)
        first_on_in_text = position_of_first_word(data)
        result[file] = {
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
