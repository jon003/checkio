""" http://www.checkio.org/mission/gate-puzzles/ 


"Likeness" coefficient for two words is measured in percentages using the following rules:
- Letter case does not matter ("A" == "a");
- If the first letters of the words are equal, then add 10%;
- If the last letters of the words are equal, then add 10%;
- Add length comparison as 
  (length_of_word1 / length_of_word2) * 30%, 
  if length_of_word1 less than or equal to length_of_word2;
  else (length_of_word2 / length_of_word1) * 30 %
- Take all unique letters from the both words in one set and count how many letters appear in the both words. 
  Add to the coefficient (common_letter_number / unique_letters_numbers) * 50;


"""

import itertools
import string
import operator

a = 'friend'
b = 'fred'

def find_uniques(word1, word2):
    uniques = ''
    for letter in word1.lower():
        if letter not in uniques:
            uniques = uniques + letter
    for letter in word2.lower():          
        if letter not in uniques:
            uniques = uniques + letter
    return uniques

def compare_likeness(word1, word2):
    percentage = 0
    # rule 1    
    if word1[0].lower() == word2[0].lower():
        percentage += 10
    # rule 2
    if word1[-1].lower() == word2[-1].lower():
        percentage += 10
    # rule 3
    len1 = len(word1)
    len2 = len(word2)
    if len1 <= len2:
        percentage += float(len1) / len2 * 30
    else:
        percentage += float(len2) / len1 * 30
    # rule 4, find uniques, then traverse for matches.
    common_letters = 0
    letter_set = find_uniques(word1, word2)
    for letter in letter_set:
        if letter in word1 and letter in word2:
            common_letters += 1
    percentage += float(common_letters) / len(letter_set) * 50

    return round(percentage, 3)


def find_word(message):
    """ input: a string of words, output: ? """
    # clean up the message so we can process.
    message = message.translate(None, string.punctuation)
    message = message.lower()

    # create list of words to iterate over.
    wordlist = message.split()

    # load up a word dictionary for the eventual values.
    worddict = {}
    worddict = worddict.fromkeys(wordlist, 0)

    # load up the likeness sums
    for word1, word2 in itertools.combinations(wordlist, 2):
        likeness = compare_likeness(word1, word2)
        worddict[word1] += likeness        
        worddict[word2] += likeness

    # turn sums into averages.
    wordcount = len(wordlist)
    for word in worddict:
        worddict[word] = worddict[word] / wordcount

    # evaluate maximum value
    match_word = max(worddict.iteritems(), key=operator.itemgetter(1))[0]

    return match_word

find_word(u"Speak friend and enter.")
# this fails on string.translate because of the difference the 'u' unicode input has on string.translate
# http://stackoverflow.com/questions/23175809/typeerror-translate-takes-one-argument-2-given-python

"""
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_word(u"Speak friend and enter.") == "friend", "Friend"
    assert find_word(u"Beard and Bread") == "bread", "Bread is Beard"
    assert find_word(u"The Doors of Durin, Lord of Moria. Speak friend and enter. "
                     u"I Narvi made them. Celebrimbor of Hollin drew these signs") == "durin", "Durin"
    assert find_word(u"Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
                     u" According to a researcher at Cambridge University.") == "according", "Research"
    assert find_word(u"One, two, two, three, three, three.") == "three", "Repeating"

"""