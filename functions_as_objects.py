def applyToEach(L, f):
    """assumes L is a list, f a function mutates L by replacing each element, e, of L by f(e)"""

    for i in range(len(L)):
        L[i] = f(L[i])


L = [1, -2, 3.4]

applyToEach(L, abs)

applyToEach(L, int)

applyToEach(L, fact)

applyToEach(L, fib)
