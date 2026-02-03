def rec(n):
    if n<1:
        print("n is less than 1")
    else:
        rec(n-1)
        print(n)

rec(5)