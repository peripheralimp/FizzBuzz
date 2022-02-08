import unittest
from fizzbuzz import fizzbuzz_func

#made these items global so I wouldnt have to declare/define in both test functions
testList = [-15, -5, -3, -2, -1, 0, 3, 4, 5, 9, 15, 16, 30, 150000]
ANSWERLIST = ['FizzBuzz', 'Buzz', 'Fizz', '', '', 'FizzBuzz', 'Fizz', '', 'Buzz', 'Fizz', 'FizzBuzz', '', 'FizzBuzz', 'FizzBuzz']
outputList = fizzbuzz_func(testList)
#testlist -> outputList, which is compared to answerList in tests below

class TestFizzbuzz(unittest.TestCase):
    #tests individual elements in outputList
    def test_elements(self):
        for i in range(len(outputList)):
            self.assertEqual(outputList[i], ANSWERLIST[i])
    #tests the whole outputList. redundant?
    def test_list(self):
        self.assertListEqual(outputList, ANSWERLIST)

if __name__ == '__main__':
    unittest.main()