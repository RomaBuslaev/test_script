import csv
import os


def read_csv(files):
    if not files:
        raise ValueError('Список files не может быть пустым.')

    files_to_read = [file for file in files if os.path.exists(file)]
    if not files_to_read:
        raise FileNotFoundError(f'Файлы {files} не найдены.')

    countries_list = []
    for file_path in files_to_read:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_reader = csv.DictReader(file, delimiter=',')
            if not file_reader.fieldnames:
                raise ValueError(f'файл {file_path} не содержит заголовков.')
            for row in file_reader:
                countries_list.append(row)
    if not countries_list:
        raise ValueError('Файлы не содержат данных.')
    return countries_list
