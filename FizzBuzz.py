#the fizzybussy project
#Gavin Webster 2/5/2022

print("""Enter an integer to add to the FizzBuzz testing list.
Enter "execute" when ready to test.""")
theList = []

while True:
    nextInt = input()
    if nextInt.isnumeric():
        theList.append(nextInt)
    elif nextInt == "execute":
        "List complete."
        break
    else:
        print('Invalid input. Enter an integer or "execute" when ready to test.')
        continue
    print("Enter next integer:")

print("\nTesting...\n")
for i in range(len(theList)):
    x = int(theList[i])
    if x % 3 == 0:
        if x % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print("Neither Fizz nor Buzz")