#!/usr/bin/python
# -*- coding: utf-8 -*-

import yaml
import argparse
import operator
from functools import reduce

def extended_euclidean(a,b,return_only_NOD=True):
    '''
    :param a,b: two numbers
    :type a,b: int > 0

    :return: NOD(a,b) or [d,u,v]
    :type: int > 0 or list of int or None
    '''
    assert isinstance(a, int) , f"type({a}) is not 'int'"
    assert isinstance(b, int) , f"type({a}) is not 'int'"
    assert (a > 0 and b > 0)  , (f"{a} and {b} must be positive")

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

def chinese_algorithm(r,m,full_asnwer_str=False):
    '''
    '''
    assert isinstance(m,list) , (f"Modules {m} must be includes to the list. "
                                "Check your .yaml file")
    assert len(m) > 1 , f"Count of modules {m} must be > 1"

    M = reduce(operator.mul,m)
    N = [int(M / m_) for m_ in m]

    d = []
    for i in range(0,len(N),1):
        d.append(extended_euclidean(N[i],m[i],return_only_NOD=False)[1])

    a = 0
    for i in range(0,len(N),1):
        a += r[i]*d[i]*N[i]

    if full_asnwer_str:
        return f'{a}={a % M}({M})'
    return a

def read_yaml_file(filename):
    assert '.yaml' in filename or '.yml' , f"{filename} is NOT YAML format"

    with open(filename, 'r') as stream:
        try:
            result = yaml.safe_load(stream)
            return (result['r'],result['m'])
        except yaml.YAMLError as exc:
            assert True, (f'Error in the read file: {exc}. '
                            'Check your .yaml file')

def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    if v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False

def params(args=None):

    parser = argparse.ArgumentParser(args)
    parser.add_argument('-in', '--input', required=True, dest='INFILE',
                        default='input.txt', type=str, help='Enter your input file with values (r and m)')
    parser.add_argument('-f', '--full', required=True, dest='FULL',
                        type=str2bool, help='Do you want look on the full answer your system? (true/false)')
    return parser.parse_args()


if __name__ == '__main__':
    p = params()
    input_file = p.INFILE
    isfull = p.FULL
    r,m = read_yaml_file(input_file)
    a = chinese_algorithm(r,m,full_asnwer_str=isfull)
    print(a)
