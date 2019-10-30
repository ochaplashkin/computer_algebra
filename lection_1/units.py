import os
import json
import unittest
import main as test_obj

# test values
a        = [1, 5, 5,  5,  10, 50, 24, 30,  34,   60, 280,  585, 680,  824, 32769, 32770, 65536]
b        = [1, 1, 5, 10,  15, 10, 42, 45, 1717, 539, 588,  360, 612,  808,   717,   717, 32769]
expected = [1, 1, 5,  5,   5, 10,  6, 15,  17,    1,  28,   45,  68,    8,     3,     1,     1]

class TestAlgorithms(unittest.TestCase):

    def run_algorithms(self,a,b,expected):
        '''
        '''
        self.assertEqual(test_obj.classic(a,b),            expected)
        self.assertEqual(test_obj.euclidean(a,b),          expected)
        self.assertEqual(test_obj.binary(a,b),             expected)
        self.assertEqual(test_obj.with_prime_numbers(a,b), expected)
        self.assertEqual(test_obj.extended_euclidean(a,b), expected)

    '''
    Negative test-cases
    '''

    def test_zero(self):
        self.run_algorithms(0,0,None)

    def test_one_of_zero(self):
        self.run_algorithms(5,0,None)

    def test_string(self):
        self.run_algorithms('5','10',None)

    def test_objects(self):
        self.run_algorithms(object,object,None)

    def test_none(self):
        self.run_algorithms(None,None,None)

    def test_negative(self):
        self.run_algorithms(-5,-10,None)

    def test_one_of_negative(self):
        self.run_algorithms(5,-10,None)

    def test_decimal(self):
        self.run_algorithms(5.0,10.0,None)

    def test_without_filename(self):
        with self.assertRaises(Exception) as context:
            test_obj.read_file()
            self.assertTrue('Could not read file:' in str(context.exception))

    def test_wrong_filename(self):
        with self.assertRaises(Exception) as context:
            test_obj.read_file("./wrong_file_name,-=.extension{_]")
            self.assertTrue('Could not read file:' in str(context.exception))

    def test_wrong_structure(self):
        d = {None:None}
        filename = "test_1.json"
        with open(filename,"w") as file:
            file.write(json.dumps(d))
            file.close()

            with self.assertRaises(Exception) as context:
                test_obj.read_file(filename)
                self.assertTrue('Could not read file:' in str(context.exception))
            os.remove(filename)

    '''
    Positive test-cases

    Note: see test values
    '''

    def test_module_functions(self):
        for i in range(0,len(a)):
            self.run_algorithms(a[i],b[i],expected[i])

    def test_cli_arguments_for_classic(self):
        for i in range(0,len(a)):
            self.assertEqual(os.system(f'python3 main.py -k classic -a {a[i]} -b {b[i]} > /dev/null'), 0)

    def test_cli_arguments_for_euclidean(self):
        for i in range(0,len(a)):
            self.assertEqual(os.system(f'python3 main.py -k euclidean -a {a[i]} -b {b[i]} > /dev/null'), 0)

    def test_cli_arguments_for_binary(self):
        for i in range(0,len(a)):
            self.assertEqual(os.system(f'python3 main.py -k binary -a {a[i]} -b {b[i]} > /dev/null'), 0)

    def test_cli_arguments_for_prime(self):
        for i in range(0,len(a)):
            self.assertEqual(os.system(f'python3 main.py -k prime -a {a[i]} -b {b[i]} > /dev/null'), 0)

    def test_cli_arguments_for_exteuclidean(self):
        for i in range(0,len(a)):
            self.assertEqual(os.system(f'python3 main.py -k exteuclidean -a {a[i]} -b {b[i]} > /dev/null'), 0)

    def test_cli_results_for_classic(self):
        for i in range(0,len(a)):
            process = os.popen(f'python3 main.py -k classic  -a {a[i]} -b {b[i]}')
            result = process.read()
            process.close()
            self.assertTrue(str(expected[i]) in result.split('=')[1])

    def test_cli_results_for_euclidean(self):
        for i in range(0,len(a)):
            process = os.popen(f'python3 main.py -k euclidean -a {a[i]} -b {b[i]}')
            result = process.read()
            process.close()
            self.assertTrue(str(expected[i]) in result.split('=')[1])

    def test_cli_results_for_binary(self):
        for i in range(0,len(a)):
            process = os.popen(f'python3 main.py -k binary  -a {a[i]} -b {b[i]}')
            result = process.read()
            process.close()
            self.assertTrue(str(expected[i]) in result.split('=')[1])

    def test_cli_results_for_prime(self):
        for i in range(0,len(a)):
            process = os.popen(f'python3 main.py -k prime  -a {a[i]} -b {b[i]}')
            result = process.read()
            process.close()
            self.assertTrue(str(expected[i]) in result.split('=')[1])

    def test_cli_results_for_exteuclidean(self):
        for i in range(0,len(a)):
            process = os.popen(f'python3 main.py -k exteuclidean  -a {a[i]} -b {b[i]}')
            result = process.read()
            process.close()
            self.assertTrue(str(expected[i]) in result.split('=')[1])

if __name__ == '__main__':
    unittest.main()