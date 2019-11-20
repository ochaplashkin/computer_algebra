#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import argparse

def is_valid_data(a,b):
    '''
    Helper function that checks input data

    :param a,b: two numbers
    :param a,b: int > 0

    :return: validation result
    :rtype: bool

    '''
    if isinstance(a, int) and isinstance(b, int):
        if a > 0 and b > 0:
            return True
    return False

def read_file(filename):
    '''
    Helper-function that reads file

    :param filename: file name
    :type filename: str

    :return: data from file
    :rtype: dict
    '''
    try:
        with open(filename) as f:
            data = json.load(f)
            return data
    except:
        raise Exception("Could not read file: %s" % filename)


def classic(a,b):
    '''
    :param a,b: two numbers > 0
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
    :param a,b: two numbers > 0
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
    :param a,b: two numbers > 0
    :type a,b: int > 0

    :return: NOD(a,b)
    :type: int > 0 or None
    '''
    if not is_valid_data(a,b):
        return None

    x,y = a,b
    d = 1
    while (x % 2 == 0) and (y % 2 == 0):
        d = d << 1
        x = x >> 1
        y = y >> 1
    while x != y:
        if x % 2 == 0:
            x = x >> 1
        if y % 2 == 0:
            y = y >> 1
        if x > y:
            x = x - y
        if x < y:
            y = y - x
    return d*x

def with_prime_numbers(a,b,prime_numbers_file='./prime_numbers.json'):
    '''
    :param a,b: two numbers > 0
    :type a,b: int > 0

    :return: NOD(a,b)
    :type: int > 0 or None
    '''
    if not is_valid_data(a,b):
        return None

    prime_numbers = read_file(prime_numbers_file)["list"]
    if not prime_numbers:
        return None

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

def params(args=None):
    parser = argparse.ArgumentParser(args)
    parser.add_argument('-k', '--kind', required=True, dest='KIND',
                        default='classic', type=str, help='Enter kind of algorithms')
    parser.add_argument('-a', '--a',    required=True, dest='A',
                        default=1, type=int, help='Enter your a value')
    parser.add_argument('-b', '--b',    required=True, dest='B',
                        default=1, type=int, help='Enter your b value')
    return parser.parse_args()

if __name__ == '__main__':
    p = params()
    kind = p.KIND
    a,b = p.A, p.B
    result = 0
    if kind == 'classic':
        result = classic(a,b)
    if kind == 'euclidean':
        result = euclidean(a,b)
    if kind == 'binary':
        result = binary(a,b)
    if kind == 'prime':
        result = with_prime_numbers(a,b)
    if kind == 'exteuclidean':
        result = extended_euclidean(a,b)

    out = f'NOD({a},{b}) = {result}'
    if not result:
        out = f'There are errors in your parametres or project structure.\nAlso, project MUST contain "prime_numbers.json" file'
    print(out)
