# Write a Python function to multiply all the numbers in a list.
def multiply_numbers(numList):
    total = 1
    for i in numList:
        total *= i
    print(total)

multiply_numbers((2, 10, 2))