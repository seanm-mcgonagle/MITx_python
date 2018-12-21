def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    min_nums = min(nums)
    max_nums = max(nums)
    unique_words = len(words)
    return (min_nums, max_nums, unique_words)


def oddTuples(aTuple):
    '''
    Write a procedure called oddTuples, which takes a tuple as input,
    and returns a new tuple as output, where every other element of
    the input tuple is copied, starting with the first one. So if test
    is the tuple ('I', 'am', 'a', 'test', 'tuple'), then evaluating
    oddTuples on this input would return the tuple ('I', 'a', 'tuple').
    '''
    odd_tups = ()

    for num in range(0, len(aTuple), 2):
        odd_tups = odd_tups + (aTuple[num],)
    return odd_tups


tupps = ('I', 'am', 'a', 'test', 'tuple',)
print(oddTuples(tupps))
