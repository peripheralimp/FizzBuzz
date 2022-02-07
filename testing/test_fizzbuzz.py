import sys
sys.path.append('../FizzBuzz')
from fizzbuzz import fizzbuzz_method
import unittest

list1 = [0, 3, 4, 5, 6, 7, 8, 9, 15, 16, 20, 30, 31]
print(fizzbuzz_method(list1))

#this should really not be here