import unittest
import fizzbuzz


class TestFizzbuzz(unittest.TestCase):
    # tests for each of the paths in fizzbuzz_func

    # given a number when it is divisible by both 3 and 5, should return 'FizzBuzz'
    def test_divisible_by_both(self):
        result = fizzbuzz.fizzbuzz_func([15])
        self.assertEqual(result, ['FizzBuzz'])

    # given a number when it is divisible by 3, should return 'Fizz'
    def test_divisible_by_3(self):
        result = fizzbuzz.fizzbuzz_func([3])
        self.assertEqual(result, ['Fizz'])

    # given a number when it is divisible by 5, should return 'Buzz'
    def test_divisible_by_5(self):
        result = fizzbuzz.fizzbuzz_func([5])
        self.assertEqual(result, ['Buzz'])

    # given a number when it is divisible by neither, should return ''
    def test_divisible_by_neither(self):
        result = fizzbuzz.fizzbuzz_func([2])
        self.assertEqual(result, [''])


if __name__ == '__main__':
    unittest.main()
