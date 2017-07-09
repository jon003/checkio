def checkio(text):
    lettercount = 0
    result = ''
    letters = list('abcdefghijklmnopqrstuvwxyz')
    text = text.lower()
    for letter in letters:
        if text.count(letter) > lettercount:
            lettercount = text.count(letter)
            result = letter
    return result

    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"Hello World!") == "l", "Hello test"
    assert checkio(u"How do you do?") == "o", "O is most wanted"
    assert checkio(u"One") == "e", "All letter only once."
    assert checkio(u"Oops!") == "o", "Don't forget about lower case."
    assert checkio(u"AAaooo!!!!") == "a", "Only letters."
    assert checkio(u"abe") == "a", "The First."
    print("Start the long test")
    assert checkio(u"a" * 9000 + u"b" * 1000) == "a", "Long."
    print("The local tests are done.")
