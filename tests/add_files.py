import csv
import os
import tempfile

import pytest

from utils.read_csv_file import read_csv


@pytest.fixture
def one_csv_file():
    with tempfile.NamedTemporaryFile(
        mode='w',
        suffix='.csv',
        delete=False,
        encoding='utf-8'
    ) as file:
        writer = csv.writer(file)
        writer.writerow(
            ['country', 'year', 'gdp', 'gdp_growth', 'inflation',
             'unemployment', 'population', 'continent']
        )
        writer.writerow(
            ['United States', '2023', '25462', '2.1',
             '3.4', '3.7', '339', 'North America']
        )
        writer.writerow(
            ['India', '2021', '3150', '8.7', '5.6', '8.0', '1410', 'Asia']
        )
        writer.writerow(
            ['France', '2022', '2779', '2.5', '5.9', '7.4', '68', 'Europe']
        )
        return file.name


@pytest.fixture
def multi_csv_files():
    files = []
    with tempfile.NamedTemporaryFile(
        mode='w', suffix='.csv', delete=False, encoding='utf-8'
    ) as file:
        writer = csv.writer(file)
        writer.writerow(['country', 'year', 'gdp', 'inflation'])
        writer.writerow(['United States', '2021', '23315', '4.7'])
        writer.writerow(['India', '2021', '3150', '5.6'])
        files.append(file.name)

    with tempfile.NamedTemporaryFile(
        mode='w', suffix='.csv', delete=False, encoding='utf-8'
    ) as file:
        writer = csv.writer(file)
        writer.writerow(['country', 'year', 'gdp', 'inflation'])
        writer.writerow(['United States', '2022', '25462', '8.0'])
        writer.writerow(['France', '2022', '2779', '5.9'])
        files.append(file.name)

    yield files
    for file in files:
        if os.path.exists(file):
            os.unlink(file)


@pytest.fixture
def parsed_data_from_one_file(one_csv_file):
    """Возвращает распарсенные данные из одного файла."""
    return read_csv([one_csv_file])
