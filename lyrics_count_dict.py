def lyrics_to_frequencies(lyrics):
	"""
	arg lyrics is a list of each word in the song e.g.

	lyrics = ['hey', 'love', 'yeah', 'yeet']

	creates a dictionary of words:frequency key:value pairs
	"""
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

def most_common_words(freqs):

	"""
	freqs is a dictionary of words:freqs 

	this function spits out a tuple containing the most common words, and the number of times they occured, e.g. (['love', 'yeah'], 4) 
	"""

	values = freqs.values() #this extracts the values from the freqs dict
	best = max(values)
	words = []

	for k in freqs:
		if freqs[k] == best:
			words.append(k)

	return (words, best)


def words_often(freqs, minTimes):

	"""
	freqs is a list
	minTimes is int, min times a word shows up

	returns a list of the words that occur more than minTimes
	"""
	

	result = []
	done = false

	while not done:

		temp = most_common_words(freqs)
		if temp[1] >= minTimes:
			result.append(temp)

			for w in temp[0]:
				del(freqs[w])
		else:
			done = True
	return result                                                        
