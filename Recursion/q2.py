# How to calculate power of a number using recursion

def powerofNumber(x,n):
    if n == 0:
        return 1
    elif n<0:
        return 1/(x * powerofNumber(x,int(n+1))) #here exponent should be increasing to converge to zero
    else:
        return x * powerofNumber(x,int(n-1))

print(powerofNumber(5,-2))