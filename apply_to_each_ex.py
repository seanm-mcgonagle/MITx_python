# apply_to_each


def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])


def abs_val(i):
    return abs(i)


testList = [1, -4, 8, -9]


print(testList)

applyToEach(testList, abs_val)
print(testList)
