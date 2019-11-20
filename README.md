# Компьютерная алгебра
[![Build Status](https://travis-ci.org/ochaplashkin/computer_algebra.svg?branch=master)](https://travis-ci.org/ochaplashkin/computer_algebra) [![codecov](https://codecov.io/gh/ochaplashkin/computer_algebra/branch/master/graph/badge.svg)](https://codecov.io/gh/ochaplashkin/computer_algebra) [![Python 3.7.3](https://img.shields.io/badge/python-3.7.3-blue.svg)](https://www.python.org/downloads/release/python-373/)
#### Установка и запуск
1. ```git clone https://github.com/ochaplashkin/computer_algebra```
2. ```python3.7 -m pip install -r requierments.txt```
3. ```cd <lection_folder>```
3. ```python3.7 main.py [requiered arguments]```
------------
#### Содержание
  - Алгоритмы нахождения НОД(а,b) в кольце Z(целые, положительные, не содержит 0):
      - [Алгоритм 1. Классический;](https://github.com/ochaplashkin/computer_algebra/blob/master/README.md#алгоритм-1-классический)
      - [Алгоритм 2. Алгоритм Евклида;](https://github.com/ochaplashkin/computer_algebra/blob/master/README.md#алгоритм-2-алгоритм-евклида)
      - [Алгоритм 3. Бинарный;](https://github.com/ochaplashkin/computer_algebra/blob/master/README.md#алгоритм-3-бинарный)
      - [Алгоритм 4. Через примарное разложение;](https://github.com/ochaplashkin/computer_algebra/blob/master/README.md#алгоритм-4-через-примарное-разложение)
      - [Алгоритм 5. Расширенный алгоритм Евклида.](https://github.com/ochaplashkin/computer_algebra/blob/master/README.md#алгоритм-5-расширенный-алгоритм-евклида)
  - Алгоритм 6. Обобщённый алгоритм Евклида для полиномов над целыми числами (не реализован)
  - [Алгоритм 7. Китайская теорема об остатках](https://github.com/ochaplashkin/computer_algebra/blob/master/README.md#алгоритм-7-китайская-теорема-об-остатках)
------------
##### Алгоритм 1. Классический

[Исходный код](https://github.com/ochaplashkin/computer_algebra/blob/master/lection_1/main.py#L39)

###### Основная идея:

Из большего числа вычитаем меньшее. Если получается 0, то значит, что числа равны друг другу и являются наибольшим общим делителем (следует выйти из цикла). Если результат вычитания не равен 0, то большее число заменяем на результат вычитания.

###### Команда запуска:

`python3.7 ./lection_1/main.py -k classic -a <первое_число> -b <второе_число>`

> Флаг -k=classic указывает на выбор классического алгоритма

##### Алгоритм 2. Алгоритм Евклида

[Исходный код](https://github.com/ochaplashkin/computer_algebra/blob/master/lection_1/main.py#L58)

###### Основная идея:

В паре чисел одно число делится с остатком на второе; делитель и полученный остаток формируют новую пару. Действие повторяется, пока один из элементов пары не обратится в 0, тогда значение другого будет равно искомому наибольшему общему делителю.

###### Команда запуска
`python3.7 ./lection_1/main.py -k euclidean -a <первое_число> -b <второе_число>`

> Флаг -k=euclidean указывает на выбор алгоритма Евклида

##### Алгоритм 3. Бинарный
[Исходный код](https://github.com/ochaplashkin/computer_algebra/blob/master/lection_1/main.py#L75)

###### Основная идея:
Основан на использовании следующих свойств НОД:
НОД(2m, 2n) = 2НОД(m, n),
НОД(2m, 2n+1) = НОД(m, 2n+1),
НОД(-m, n) = НОД(m, n).

Описание алгоритма:
1. НОД(0, n) = n; НОД(m, 0) = m; НОД(m, m) = m;
2. НОД(1, n) = 1; НОД(m, 1) = 1;
3. Если m, n чётные, то НОД(m, n) = 2*НОД(m/2, n/2);
4. Если m чётное, n нечётное, то НОД(m, n) = НОД(m/2, n);
5. Если n чётное, m нечётное, то НОД(m, n) = НОД(m, n/2);
6. Если m, n нечётные и n > m, то НОД(m, n) = НОД((n-m)/2, m);
7. Если m, n нечётные и n < m, то НОД(m, n) = НОД((m-n)/2, n);

###### Команда запуска
`python3.7 ./lection_1/main.py -k binary -a <первое_число> -b <второе_число>`

> Флаг -k=binary указывает на выбор Бинарного алгоритма

##### Алгоритм 4. Через примарное разложение
[Исходный код](https://github.com/ochaplashkin/computer_algebra/blob/master/lection_1/main.py#L103)

###### Основная идея:

НОД можно найти из разложения чисел на простые множители.

> *a = m1 * m2 * m3 * ... * mN*
>где m – простые числа

НОД будет равен произведению простых множителей, общих для обоих чисел.

Например:

>24 = (2) * 2 * 2 * (3)
>54 = (2) * (3) * 3 * 3

Общие множители выделены скобками

> НОД(24, 54) = 2 * 3 = 6

###### Команда запуска
`python3.7 ./lection_1/main.py -k prime -a <первое_число> -b <второе_число>`

> Флаг -k=prime указывает на выбор алгоритма с помощью разложения числа на простые множители

##### Алгоритм 5. Расширенный алгоритм Евклида
[Исходный код](https://github.com/ochaplashkin/computer_algebra/blob/master/lection_1/main.py#L137)

###### Основная идея:

Пусть **d** - наибольший общий делитель чисел a и b. Тогда выражение  **ax+by** всегда кратно **d**. Оказывается, что можно подобрать такие числа **x** и **y**, что **ax+by=d**.

###### Команда запуска
`python3.7 ./lection_1/main.py -k exteuclidean -a <первое_число> -b <второе_число>`

> Флаг -k=exteuclidean указывает на выбор расширенного алгоритма Евклида

##### Алгоритм 7. Китайская теорема об остатках
[Исходный код](https://github.com/ochaplashkin/computer_algebra/blob/master/lection_3/main.py#L32)

###### Основная идея:

Если натуральный числа (a1,a2,..,aN) попарно взаимно простые, то для любых целых (r1,r2,..rN) таких, что 0 <= ri < ai при всех i={1,n}, найдется число N, которое при делении на ai дает остаток ri  при всех i={1,2,..,n}. Более того, если найдутся два таких числа N1 и N2, то N1 (сравнимо с) N2 по модулю M=(a1 * a2 * a3 ... * aN)

###### Команда запуска
`python3.7 ./lection_3/main.py -in <путь_до_входного_файла> [-f <отображать полный ответ?>]`

> Организация входного файла YAML формата [пример](https://github.com/ochaplashkin/computer_algebra/blob/master/lection_3/input.yaml):

```yaml
r:
  - значение 1
  - значение 2
  - ...
m:
  - значение 1
  - значение 2
  - ...
```

> Флаг -f= yes / no - позволяет включить / выключить вывод полного ответа решения на экран в виде <ответ> = <остаток> (mod <M>)
