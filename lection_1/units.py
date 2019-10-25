import main as test_obj
import unittest

class TestAlgorithms(unittest.TestCase):

    def run_algorithms(self,a,b,expected):
        '''
        '''
        self.assertEqual(test_obj.classic(a,b),            expected)
        self.assertEqual(test_obj.euclidean(a,b),          expected)
        # self.assertEqual(test_obj.binary(a,b),             expected)
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

    '''

    Positive test-cases

    '''
    def test_positive(self):
        a        = [1, 5, 5,  5,  10, 50, 30,  34,   60,  824, 32769, 32770, 65536]
        b        = [1, 1, 5, 10,  15, 10, 45, 1717, 539,  808,   717,   717, 32769]
        expected = [1, 1, 5,  5,   5, 10, 15,  17,    1,    8,     3,     1,     1]

        for i in range(0,len(a)):
            self.run_algorithms(a[i],b[i],expected[i])

if __name__ == '__main__':
    unittest.main()