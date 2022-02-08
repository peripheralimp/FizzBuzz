#the fizzybussy project
#Gavin Webster 2/5/2022

def fizzbuzz_func(inputList):
    outputList = []
    for item in inputList:
        if item % 3 == 0 and item % 5 == 0:
            outputList.append("FizzBuzz")
        elif item % 3 == 0:
            outputList.append("Fizz")
        elif item % 5 == 0:
            outputList.append("Buzz")
        else:
            outputList.append("")
    return outputList

