# def a func to find the max of 3 nums
def max_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print("1st number is largest")
    elif num2 > num3 and num2 > num1:
        print("2nd number is largest")
    else:
        print("3rd number is largest")

max_num(15, 22, 9)