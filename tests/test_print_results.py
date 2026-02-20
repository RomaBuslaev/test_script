from utils.print_results import print_results


class TestPrintResults:
    """Тест вывода результатов."""

    def test_print_results_normal(self, capsys):
        """Тест вывода результатов."""
        results = [
            ('United States', 25462.0), ('France', 2779.0), ('India', 3150.0)]

        print_results(results)
        captured = capsys.readouterr()
        assert "country" in captured.out
        assert "gdp" in captured.out
        assert "United States" in captured.out
        assert "France" in captured.out
        assert "India" in captured.out

    def test_print_results_empty(self, capsys):
        """Тест вывода при пустых результатах."""
        print_results([])
        captured = capsys.readouterr()
        assert "Нет данных для отображения" in captured.out
