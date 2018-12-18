def stripper(text):
    text = text.lower()
    fixed_text = ''
    for letter in text:
        if letter in 'abcdefghijklmnopqrstuvwxyz':
            fixed_text += letter
    return fixed_text


print(stripper('fuck yall'))
