copy_hand = {'t': 2, 'b': 1, 'f': 1, 'u': 1}
word = 'butt'
is_from_hand = True

    for letter in word:
        try:
            copy_hand[letter] -= 1
        except KeyError:
            is_from_hand = False
            break

        if copy_hand[letter] < 0:
            is_from_hand = False
            break
    print(is_from_hand)
