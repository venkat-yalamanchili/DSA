# GCD of two numbers
# Recursive approach

def gcd(a,b):
    assert int(a) == a and int(b) ==b, "The numbers must be integer only"
    if a < 0 :
        a = a * -1 # make it positive and then run the algo
    if b < 0 :
        b = b * -1
    if b == 0:
        return a
    else:
        return gcd(b,a%b)  # Euclid's Algo

print(gcd(18,48))

# Iterative approach (if you want you can handle the -ve number as above)
def i_gcd(a,b):
    assert int(a) == a and int(b) ==b, "The numbers must be integer only"
    while(b):
        a, b = b, (a%b)
    return a

print(i_gcd(48,18))