#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import yaml
import unittest
import main as test_obj

r = [
    [3,7],
    [2,4],
    [3,1,0],
    [1,2,6],
    [2,3,2],
    [2,15,5],
    [7,-1,3],
    [3,1,12],
    [7,-1,3,4]
]
m = [
    [5,17],
    [13,19],
    [5,7,2],
    [2,3,7],
    [3,5,7],
    [5,17,12],
    [8,11,15],
    [8,11,15],
    [8,11,15,7]
]
x = [
    143,
    80,
    -62,
    -43,
    23,
    1817,
    -1497,
    5787,
    34143
]

full_x = [
    '143=58(85)',
    '80=80(247)',
    '-62=8(70)',
    '-43=41(42)',
    '23=23(105)',
    '1817=797(1020)',
    '-1497=1143(1320)',
    '5787=507(1320)',
    '34143=6423(9240)'
]

test_bool     = ['yes', 'true', 't', 'y', '1', 'no', 'false', 'f', 'n', '0']
expected_bool = [True ,  True ,True,True,True, False, False,False,False,False]

class TestChineseModule(unittest.TestCase):

    def setup_file(self,filename):
        test_r = [1,2,3]
        test_m = [2,4,6]
        test_data = {
            'r':r,
            'm':m
        }
        with open(filename,"w") as file:
            yaml.dump(test_data, file, default_flow_style=False)
            file.close()

    def test_parametrize(self):
        for i in range(0,len(r),1):
            answer = test_obj.chinese_algorithm(r[i],m[i])
            self.assertEqual(answer,x[i])
    def test_parametrize_with_full_answer(self):
        for i in range(0,len(r),1):
            answer = test_obj.chinese_algorithm(r[i],m[i],full_asnwer_str=True)
            self.assertEqual(answer,full_x[i])

    def test_extended_euclidean(self):
        '''
        simple test for the test-coverage
        More tests see in lection_1 folder -> units.py
        '''
        self.assertEqual(test_obj.extended_euclidean(280,588), 28)

    def test_read_yaml_format(self):
        filename = 'unitest.yaml'
        self.setup_file(filename)

        a = test_obj.read_yaml_file(filename)

        self.assertEqual(a[0],r)
        self.assertEqual(a[1],m)

        os.remove(filename)

    def test_read_yml_format(self):
        filename = 'unittest.yml'
        self.setup_file(filename)

        a = test_obj.read_yaml_file(filename)

        self.assertEqual(a[0],r)
        self.assertEqual(a[1],m)

        os.remove(filename)

    def test_str2bool_parametrize(self):
        for i in range(0,len(r),1):
            response_bool = test_obj.str2bool(test_bool[i])
            self.assertEqual(response_bool,expected_bool[i])

if __name__ == '__main__':
    unittest.main()