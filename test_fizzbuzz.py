import unittest
import fizzbuzz as fz


class TestFizzbuzz(unittest.TestCase):
    # tests for each of the paths in fizzbuzz_func

    # given a number when it is divisible by both 3 and 5, should return 'FizzBuzz'
    def test_divisible_by_both(self):
        self.assertEqual(fz.fizzbuzz_func(15), 'FizzBuzz')

    # given a number when it is divisible by 3, should return 'Fizz'
    def test_divisible_by_3(self):
        self.assertEqual(fz.fizzbuzz_func(3), 'Fizz')

    # given a number when it is divisible by 5, should return 'Buzz'
    def test_divisible_by_5(self):
        self.assertEqual(fz.fizzbuzz_func(5), 'Buzz')

    # given a number when it is divisible by neither, should return ''
    def test_divisible_by_neither(self):
        self.assertEqual(fz.fizzbuzz_func(1), '')


if __name__ == '__main__':
    unittest.main()
