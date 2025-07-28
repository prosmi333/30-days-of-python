# Level 1
# Exercise 1
from collections import Counter
import json


def word_line_counter(filename):
    if type(filename) != "str":
        print("File name has to be a string. Please change it")
        exit
    file = open(filename)
    lines = file.readlines()
    words = file.read()
    file.close()
    print(f"There are {len(words)} words in this file")
    print(f"There are {len(lines)} lines of text in this file")


# Exercise 2


def top_ten_languages_from_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        all_languages = []
        for country in data:
            all_languages.extend(country.get("languages", []))

        language_counts = Counter(all_languages)
        return language_counts.most_common(10)

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except json.JSONDecodeError:
        print(f"Invalid JSON format in: {file_path}")
        return []


# Exercise 3


def top_ten_populated_countries(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        sorted_countries = sorted(
            data, key=lambda x: x['population'], reverse=True)

        return sorted_countries[:10]

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except json.JSONDecodeError:
        print(f"Invalid JSON format in: {file_path}")
        return []
    except KeyError:
        print("Missing 'population' field in one or more entries.")
        return []
