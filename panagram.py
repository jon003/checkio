import string
def check_pangram(text):
    fulldict = dict.fromkeys(string.ascii_lowercase, 1)
    newdict = {}
    for letter in list(text):
        if letter.lower() in string.ascii_lowercase:
            newdict[letter.lower()] = 1
    if newdict == fulldict:
        return True
    else:
        return False

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
