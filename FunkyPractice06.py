# Write a Python program to reverse a string.
def strRevers(charString):
    rstr = ''
    index = len(charString)
    while index > 0:
        rstr += charString[index - 1]
        index = index - 1
    print(rstr)


strRevers("abc def ghi jkl")