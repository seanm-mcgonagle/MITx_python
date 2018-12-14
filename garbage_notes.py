x = 12


def g(x):
    x = x + 1.  # x = 13

    def h(y):
        return x + y  # 13 + y
    return h(6)


print(g(x))
