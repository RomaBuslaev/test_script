# Тестовый script
    Скрипт нужен для обработки данных по странам. Можно найти средние значения 
для разных данных и т.д.
    Пример работы можно увидеть в script_example.png.

## Установка и работа
1. Клонировать репозиторий:
git clone https://github.com/RomaBuslaev/test_script.git
2. Перейти директория приложения:
cd test_script
3. Создать виртуальное окружение:
python -m venv venv # Команда для Windows
python3 -m venv venv # Команда для Linux и macOS
4. Активировать виртуальное окружение:
source venv/Scripts/activate # Команда для Windows
source venv/bin/activate # Для Linux и macOS
5. Установить модули из файла requirementst.txt:
pip install -r requirements.txt
6. Попробовать скрипт в работе:
python main.py --files economic1.csv economic2.csv --report average-gdp # Команда для Windows
python3 main.py --files economic1.csv economic2.csv --report average-gdp # Для Linux и macOS

### Возможность добавить дополнительную обработку данных
    Для добавления новых функций достаточно написать дополнительную функцию с
нужнымы обработками и добавить эти данные в переменные в main.py
    В данном скрипте добавлена дополнительная функция, чтобы показать, как быстро
можно добавить дополнительную функциональность данному скрипту.
Для дополнительной функции:
python main.py --files economic1.csv economic2.csv --report average_inflation # Команда для Windows
python3 main.py --files economic1.csv economic2.csv --report average_inflation # Для Linux и macOS

Буслаев Роман [RomaBuslaev](https://github.com/RomaBuslaev)
Для связи (romainbuslaev@yandex.ru)