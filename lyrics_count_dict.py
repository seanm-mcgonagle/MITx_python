def lyrics_to_frequencies(lyrics):
	"""argument lyrics will be a string separated by spaces"""
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict


