import argparse

from reports.get_average_values import average_gdp, average_inflation
from utils.print_results import print_results
from utils.read_csv_file import read_csv


CHOICES = ['average-gdp', 'average_inflation']
REPORT_FUNCTIONS = {
    'average-gdp': average_gdp,
    'average_inflation': average_inflation
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--files',
        nargs='+',
        required=True
    )
    parser.add_argument(
        '--report',
        choices=CHOICES,
        default='average-gdp'
    )
    args = parser.parse_args()
    data = read_csv(args.files)
    report_func = REPORT_FUNCTIONS[args.report]
    results = report_func(data)
    print_results(results)


if __name__ == '__main__':
    main()
