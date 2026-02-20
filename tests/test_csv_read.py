import os

from tests.add_files import one_csv_file, multi_csv_files
from utils.read_csv_file import read_csv


class TestReadCSVFile:
    def test_read_one_csv(self, one_csv_file):
        """Тест чтения одного CSV файла."""
        result = read_csv([one_csv_file])

        assert len(result) == 3
        assert result[0]['country'] == 'United States'
        assert result[0]['gdp'] == '25462'
        assert result[0]['continent'] == 'North America'

        assert result[1]['country'] == 'India'
        assert result[1]['gdp'] == '3150'

        assert result[2]['country'] == 'France'
        assert result[2]['gdp'] == '2779'

    def test_read_multiple_csv(self, multi_csv_files):
        """Тест чтения нескольких CSV файлов."""
        result = read_csv(multi_csv_files)
        assert len(result) == 4
        us_data = [row for row in result if row['country'] == 'United States']
        assert len(us_data) == 2
        india_data = [row for row in result if row['country'] == 'India']
        assert len(india_data) == 1
        france_data = [row for row in result if row['country'] == 'France']
        assert len(france_data) == 1
