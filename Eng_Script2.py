# William Eng
# weng2@oakland.edu
# This Python program computes the i-th item in a Fibonacci sequence

def fib(i):
    try:
        i = int(i)
        if i <= 0:
            return "Error: Invalid input (Negative Number or 0).  Only positive integers"
        elif i == 1:
            return 0
        elif i == 2:
            return 1
        # elif i == 3:
        #     return 1
        else:
            return fib(i-1) + fib(i-2)
    except ValueError:
        return "Invalid input (Not a number).  Only positive integers"

userInput = input("Give me a positive integer ")
print("The {}-th item you get from a Fibonacci sequence is {}".format(userInput,fib(userInput)))

# Test case
# 20 4181
# a invalid
# -5 invalid
# 0 invalid
# 1 invalid