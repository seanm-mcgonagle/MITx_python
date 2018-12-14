def mult(a, b):
    if b == 1:
        return a
    else:
        return a + mult(a, b - 1)


print(mult(2, 3))


def factorial(n):
        # factorial of n is  n! = n*(n-1)! = n*(n-1)*(n-2)!...
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(3))
