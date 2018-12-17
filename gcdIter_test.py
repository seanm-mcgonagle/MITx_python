def gcdIter(a, b):
        if a > b:
                test = float(b)
                high = float(a)
                low = float(b)

        else:
                test = float(a)
                high = float(b)
                low = float(a)

        while test >= 1:
                if high % test == 0 and low % test == 0:
                        return int(test)
                test = test - 1.


print(gcdIter(6, 12))
