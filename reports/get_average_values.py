from collections import defaultdict
from operator import itemgetter


def average_gdp(files):
    """Получение ср значения для ВВП по странам и их сортировка по убыванию."""
    countries_avg_gdp = defaultdict(list)
    for row in files:
        country = row['country']
        gdp = int(row['gdp'])
        countries_avg_gdp[country].append(gdp)
    result = {}
    for country, dgp in countries_avg_gdp.items():
        avg_gdp = sum(dgp) / len(dgp)
        result[country] = round(avg_gdp, 2)
    return sorted(result.items(), key=itemgetter(1), reverse=True)


def average_inflation(files):
    """Получение ср. значения для инфляции и их сортировка по убыванию."""
    countries_avg_inflation = defaultdict(list)
    for row in files:
        country = row['country']
        inflation = float(row['inflation'])
        countries_avg_inflation[country].append(inflation)
    result = {}
    for country, inflation in countries_avg_inflation.items():
        avg_inflation = sum(inflation) / len(inflation)
        result[country] = round(avg_inflation, 2)
    return sorted(result.items(), key=itemgetter(1), reverse=True)
