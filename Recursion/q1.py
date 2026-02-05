# How to find the sum of digits of a positive integer number using recurssion

def sumofDigits(n):
    if not isinstance(n,int) or n<0:
        return "n should be non negative integer"
    elif n == 0:
        return 0
    return int(n%10)+sumofDigits(int(n//10))

print(sumofDigits(10))