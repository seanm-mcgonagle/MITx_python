def fib(n):
    if n == 1:
        return 1

    elif n == 2:
        return 2

    else:
        return fib(n - 1) + fib(n - 2)
        #[fib(5-1)] + [fib(5-2)]
        #[{fib(4-1)} + fib(4-2)] + [fib(3-1) + fib(3-2)]
        #[{fib(3-1) + fib(3-2)} + 2] + [2 + 1]
        #[2 + 2 +1] + [2 + 1] = 2 + 2 + 2 + 1 + 1 = 8


print(fib(5))


# here's a more clever way to do this with dictionaries

def fib_efficient(num, dict):
    """
    num is the number of fib terms you want 
    dict is a dictionary, which contains your base case
    """

    if num in dict:
        return dict[num]

    else:
        ans = fib_efficient(num - 1, dict) + fib_efficient(num - 2, dict)

        dict[num] = ans
        return ans


dict = {1: 1, 2: 2}  # base cases
print(fib_efficient(6, dict))
