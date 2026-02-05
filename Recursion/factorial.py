def rec(n):
    if n<1:
        print("n is less than 1")
    else:
        rec(n-1)
        print(n)

def factorial(n):
    if not isinstance(n, int):
        return "Input must be an integer"
    if n <=1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3.8))