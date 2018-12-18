def isPalendrome(text):

    def stripper(text):
        text = text.lower()
        fixed_text = ''
        for letter in text:
            if letter in 'abcdefghijklmnopqrstuvwxyz':
                fixed_text += letter
        return fixed_text

    def isPal(text):
        if len(text) <= 1:
            return True
        else:
            return text[0] == text[-1] and isPal(text[1:-1])

    return isPal(stripper(text))


print(isPalendrome('heck Yes'))
