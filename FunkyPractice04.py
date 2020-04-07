# Write a Python function to sum all the numbers in a list.

def add_numbers(numList):
    total = 0
    for i in numList:
        total += i
    print(total)

# call the func with a 'list' of numbers as 'arguments'
# #(notice the extra parentheses, which are used to create the 'list')
add_numbers((4, 3, 10))