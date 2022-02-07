#the fizzybussy project
#Gavin Webster 2/5/2022

def fizzBuzz(inputList):
    outputList = []
    for item in inputList:
        if item % 3 == 0:
            if item % 5 == 0:
                outputList.append("FizzBuzz")
            else:
                outputList.append("Fizz")
        elif item % 5 == 0:
            outputList.append("Buzz")
        else:
            outputList.append("")
    return outputList
