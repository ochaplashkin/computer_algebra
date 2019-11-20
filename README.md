# Компьютерная алгебра
[![Build Status](https://travis-ci.org/ochaplashkin/computer_algebra.svg?branch=master)](https://travis-ci.org/ochaplashkin/computer_algebra) [![codecov](https://codecov.io/gh/ochaplashkin/computer_algebra/branch/master/graph/badge.svg)](https://codecov.io/gh/ochaplashkin/computer_algebra) [![Python 3.7.3](https://img.shields.io/badge/python-3.7.3-blue.svg)](https://www.python.org/downloads/release/python-373/)

#### Установка и запуск
1. ```git clone https://github.com/ochaplashkin/computer_algebra```
2. ```python3.7 -m pip install -r requierments.txt```
3. ```python3.7 ./<lection_folder>/main.py [optional arguments]```

#### Содержание
  - Алгоритмы нахождения НОД(а,b) в кольце Z(целые, положительные, не содержит 0):
    - ```python3.7 ./lection_1/main.py -k <algorithm> -a <first_number> -b <second_number>```
      - [Алгоритм 1. Классический;](https://github.com/ochaplashkin/computer_algebra/blob/master/lection_1/main.py#L39)
        - ```python3.7 ./lection_1/main.py -k classic -a 10 -b 5```
      - [Алгоритм 2. Алгоритм Евклида;](https://github.com/ochaplashkin/computer_algebra/blob/master/lection_1/main.py#L58)
        - ```python3.7 ./lection_1/main.py -k euclidean -a 10 -b 5```
      - [Алгоритм 3. Бинарный;](https://github.com/ochaplashkin/computer_algebra/blob/master/lection_1/main.py#L75)
        - ```python3.7 ./lection_1/main.py -k binary -a 10 -b 5```
      - [Алгоритм 4. Через примарное разложение;](https://github.com/ochaplashkin/computer_algebra/blob/master/lection_1/main.py#L103)
        - ```python3.7 ./lection_1/main.py -k prime -a 10 -b 5```
      - [Алгоритм 5. Расширенный алгоритм Евклида.](https://github.com/ochaplashkin/computer_algebra/blob/master/lection_1/main.py#L137)
        - ```python3.7 ./lection_1/main.py -k exteuclidean -a 10 -b 5```
  - Алгоритм 6. Обобщённый алгоритм Евклида для полиномов над целыми числами (не реализован)
  - [Алгоритм 7. Китайская теорема об остатках](https://github.com/ochaplashkin/computer_algebra/blob/master/lection_3/main.py#L32)
   - ```python3.7 ./lection_3/main.py -in <path_to_your_file> [-f <show full answer>]```
   - Входной файл должен быть в формате YAML и иметь аналогичную структуру input.yaml.
