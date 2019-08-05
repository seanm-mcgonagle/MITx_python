def biggest(aDict):
    """
    returns the key corresponding to the entry with the largest number of values associated with it
    """

    length_dict = {}
    # e.g. {'a': [1], 'b': [1], 'c': [1], 'd': [4]}
    for key in aDict:
        length_dict[key] = [len(aDict[key])]

    my_values = length_dict.values()
    largest_v = max(my_values)

    biggest_keys = []

    for key in length_dict:
        if length_dict[key] == largest_v:
            biggest_keys.append(key)

    final_answer = ''.join(biggest_keys)

    return(final_answer)


animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
animals['d'].append('dingus')


print(biggest(animals))
