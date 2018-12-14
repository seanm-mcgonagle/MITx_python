"""Write an iterative function iterPower(base, exp) that calculates the 
exponential  by simply using successive multiplication. 
For example, iterPower(base, exp) should compute  by multiplying base times itself exp times.
Write such a function below.

This function should take in two values - base can be a float or an integer; 
exp will be an integer  0. It should return one numerical value. 
Your code must be iterative - use of the ** operator is not allowed."""

# base^exp= base * base * base * base (exp number of times)


def iterPower(base, exp):
    answer = 1
    counter = 0
    for i in range(exp):
        answer = answer * base
        counter = counter + 1
        print(counter)
    return answer


print(iterPower(6, 6))


def iterPower_v2(base, exp):
    answer = 1
    while exp > 0:

        answer = answer * base
        exp -= 1
    return answer


print(iterPower_v2(6, 6))


def recurPower(base, exp):
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)


print(recurPower(6, 6))
