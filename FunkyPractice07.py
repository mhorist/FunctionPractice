# Write a Python function to check whether a number is in a given range.
def isInRange(num_range):
    if num_range in range(1, 10):
        print("It is in the range.")
    else:
        print("It is not in the range.")

x = input("Enter a number: ")
isInRange(int(x))