#!/usr/bin/python
# -*- coding: utf-8 -*-
import json


def is_valid_data(a,b):
    '''
    Helper
    '''
    if isinstance(a, int) and isinstance(b, int):
        if a > 0 and b > 0:
            return True
    return False


def classic(a,b):
    '''
    :param a,b: two numbers
    :type a,b: int > 0

    :return: NOD(a,b)
    :type: int > 0 or None
    '''
    if not is_valid_data(a,b):
        return None

    x,y = a,b
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return x

def euclidean(a,b):
    '''
    :param a,b: two numbers
    :type a,b: int > 0

    :return: NOD(a,b)
    :type: int > 0 or None
    '''
    if not is_valid_data(a,b):
        return None

    x,y = a,b
    while y != 0:
        r = x % y
        x,y = y,r
    return x

def binary(a,b):
    '''
    :param a,b: two numbers
    :type a,b: int > 0

    :return: NOD(a,b)
    :type: int > 0 or None
    '''
    if not is_valid_data(a,b):
        return None

    x,y = a,b
    d = 1
    while (x % 2 == 0) and (y % 2 == 0):
        d = 2 * d
        x = x / 2
        y = y / 2
        while x == y:
            if x % 2 == 0:
                x = x / 2
                continue
            if y % 2 == 0:
                y = y / 2
                continue
            if x > y:
                x = x - y
                continue
            if x < y:
                y = y - x
                continue
    return d*x

def with_prime_numbers(a,b):
    '''
    #TODO: check it
    '''
    if not is_valid_data(a,b):
        return None

    with open('./prime_numbers.json') as f:
        prime_numbers = json.load(f)['list']

    x,y = a,b
    d = 1
    _n = 0
    p = prime_numbers[_n]
    while (x != 1) and (y != 1):
        while(x % p == 0) and (y % p == 0):
            d = d * p
            x = x / p
            y = y / p
        while x % p == 0:
            x = x / p
        while y % p == 0:
            y = y / p
        _n += 1
        if _n > len(prime_numbers):
            return None
        p = prime_numbers[_n]
    return d


def extended_euclidean(a,b,return_only_NOD=True):
    '''
    :param a,b: two numbers
    :type a,b: int > 0

    :return: NOD(a,b) or [d,u,v]
    :type: int > 0 or list of int or None
    '''
    if not is_valid_data(a,b):
        return None
    x = [a,1,0]
    y = [b,0,1]
    while y[0] != 0:
        q = x[0] // y[0]
        r = [x[i] - q*y[i] for i in range(0,3)]
        x = [element for element in y]
        y = [element for element in r]
    if return_only_NOD:
        return x[0]
    return x

if __name__ == '__main__':
    main()