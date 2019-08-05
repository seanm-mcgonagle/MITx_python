def biggest_better(aDict):
    if len(aDict) == 0:
        return none
    else:
        return max(aDict)


animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
animals['d'].append('dingus')


print(biggest_better(animals))
