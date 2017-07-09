"""
http://www.checkio.org/mission/striped-words/

You are given a block of text with different words. 
These words are separated by white-spaces and punctuation marks. 

Numbers are not considered words in this mission (a mix of letters and digits is not a word either). 

You should count the number of words (striped words) where the vowels with consonants are 
alternating, that is; words that you count cannot have two consecutive vowels or consonants. 
The words consisting of a single letter are not striped -- do not count those. 
Casing is not significant for this mission.

"""


VOWELS = "AEIOUYaeiouy"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz"
PUNCTUATION = (',', ':', ';', '.', '!', '`', '-', ')', '(', '?', "'", '"')
NUMBERS = (1,2,3,4,5,6,7,8,9,0)
        

def is_word(word):
	""" Takes a word, determines if it is a real word, according to the rules listed """
	if len(word) <= 1:
		return False
	for letter in word:
		if letter in NUMBERS:
			return False
	return True

def all_vowel(word):
	""" Takes a string, checks to see if every letter in the string is a vowel. """
	for letter in word:
		if letter not in VOWELS:
			return False
	return True

def all_cons(word):
	""" Takes a string, checks to see if every letter in the string is a consonant. """
	for letter in word:
		if letter not in CONSONANTS:
			return False
	return True

def is_striped(word):
	a = word[0::2]
	b = word[1::2] 
	if all_vowel(a) and all_cons(b):
		return True
	elif all_vowel(b) and all_cons(a):
		return True
	else:
		return False

def checkio(text):
	striped = 0
	for char in PUNCTUATION:
          text = text.replace(char,' ')
	for word in text.split():
		if is_word(word) and is_striped(word):
			striped += 1
	return striped


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"My name is ...") == 3, "All words are striped"
    assert checkio(u"Hello world") == 0, "No one"
    assert checkio(u"A quantity of striped words.") == 1, "Only of"
    assert checkio(u"Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"

