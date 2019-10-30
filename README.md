# Компьютерная алгебра
[![Build Status](https://travis-ci.org/ochaplashkin/computer_algebra.svg?branch=master)](https://travis-ci.org/ochaplashkin/computer_algebra) [![codecov](https://codecov.io/gh/ochaplashkin/computer_algebra/branch/master/graph/badge.svg)](https://codecov.io/gh/ochaplashkin/computer_algebra)

#### Установка и запуск
1. ```git clone https://github.com/ochaplashkin/computer_algebra```
2. ```python3.7 -m pip install -r requierments.txt```
3. ```python3.7 <lection_folder>/main.py [optional arguments]```

#### Содержание
  - Лекция 1. Алгоритмы нахождения НОД(а,b) в кольце Z(целые, положительные, не содержит 0):
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
