def fibonacci(n):
    if not isinstance(n,int) or n<0:
        return "n should be non negative integer"
    elif n in [0,1]:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(4))

# Iterative approach
def print_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        # Update a and b simultaneously
        a, b = b, a + b
    # print(a) if you only want that number insted of series

# Example: Print the first 10 numbers
print_fibonacci(4)