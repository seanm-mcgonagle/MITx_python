animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
animals['d'].append('dingus')


def how_many(aDict):
    """
    returns the sum of the number of values associated with a dictionary
    """

    values = aDict.values()

    total_length = 0
    for value in values:
        total_length += len(value)

    return total_length


print(how_many(animals))
