from reports.get_average_values import average_gdp
from utils.read_csv_file import read_csv
from tests.add_files import one_csv_file, multi_csv_files, parsed_data_from_one_file


class TestAverageValues:
    def test_average_gdp_from_one_file(self, parsed_data_from_one_file):
        """Тест расчета среднего ВВП из одного файла."""
        result = average_gdp(parsed_data_from_one_file)
        assert isinstance(result, list)
        assert len(result) == 3
        result_dict = dict(result)
        assert result_dict['United States'] == 25462.0
        assert result_dict['India'] == 3150.0
        assert result_dict['France'] == 2779.0
        assert result[0][0] == 'United States'
        assert result[1][0] == 'India'
        assert result[2][0] == 'France'

    def test_average_gdp_from_multiple_files(self, multi_csv_files):
        """Тест расчета среднего ВВП из нескольких файлов."""
        data = read_csv(multi_csv_files)
        result = average_gdp(data)
        assert len(result) == 3
        result_dict = dict(result)
        expected_us = (23315 + 25462) / 2
        assert result_dict['United States'] == round(expected_us, 2)
        assert result_dict['India'] == 3150
        assert result_dict['France'] == 2779.0

    def test_average_gdp_empty_input(self):
        """Тест расчета среднего ВВП с пустыми данными."""
        result = average_gdp([])
        assert result == []

    def test_average_gdp_for_single_country(self):
        """Тест расчета среднего ВВП для одной страны с несколькими записями."""
        data = [
            {'country': 'United States', 'gdp': '25462', 'inflation': '3.4'},
            {'country': 'United States', 'gdp': '27357', 'inflation': '3.4'},
        ]
        result = average_gdp(data)
        assert len(result) == 1
        expected = (25462 + 27357) / 2
        assert result[0] == ('United States', round(expected, 2))
