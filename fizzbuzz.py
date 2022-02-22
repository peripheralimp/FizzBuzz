# the fizzybussy project
# Gavin Webster 2/5/2022

def fizzbuzz_func(x):
    try:
        x = int(x)
    except ValueError:
        print('Not a valid input')
        return
    if x % 3 == 0 and x % 5 == 0:
        return 'FizzBuzz'
    elif x % 3 == 0:
        return 'Fizz'
    elif x % 5 == 0:
        return 'Buzz'
    else:
        return ''
