from tabulate import tabulate


def print_results(results):
    """Форматирование вывода результата."""
    if not results:
        print("Нет данных для отображения")
        return
    table_data = []
    for i, (country, gdp) in enumerate(results, 1):
        table_data.append([i, country, f"{gdp:.2f}"])

    print(tabulate(
        table_data,
        headers=["country", "gdp"],
        tablefmt="pretty",
        colalign=("center", "left", "right")
    ))
