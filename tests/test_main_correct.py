from main import main
from tests.add_files import one_csv_file, multi_csv_files


class TestMain:
    def test_main_average_gdp_with_one_file(
            self, one_csv_file, monkeypatch, capsys):
        """Тест main с одним файлом и отчётом average-gdp ."""

        test_args = ['prog', '--files', one_csv_file, '--report', 'average-gdp']
        monkeypatch.setattr('sys.argv', test_args)

        main()

        captured = capsys.readouterr()

        assert "country" in captured.out
        assert "gdp" in captured.out
        assert "United States" in captured.out
        assert "India" in captured.out
        assert "France" in captured.out

        assert "25462.0" in captured.out
        assert "3150.0" in captured.out
        assert "2779.0" in captured.out

    def test_main_average_gdp_with_multiple_files(
            self, multi_csv_files, monkeypatch, capsys):
        """Тест main с несколькими файлами и отчётом average-gdp."""

        test_args = (['prog', '--files'] + multi_csv_files +
                     ['--report', 'average-gdp'])
        monkeypatch.setattr('sys.argv', test_args)

        main()

        captured = capsys.readouterr()
        assert "United States" in captured.out
        assert "India" in captured.out
        assert "France" in captured.out
        assert "24388.5" in captured.out
        assert "3150.0" in captured.out
        assert "2779.0" in captured.out
