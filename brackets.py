def checkio(expression):
	""" Check to see if the bracketing runs in a valid sequence. """

	blist = []

	for char in expression:
		if char in ['(', '{', '[']:				# load queue
			blist.append(char)
		elif char == ')' and blist and blist[-1] == '(': 	# clean queue of the 3 valid matches  
			del(blist[-1])
		elif char == '}' and blist and blist[-1] == '{':
			del(blist[-1])
		elif char == ']' and blist and blist[-1] == '[':
			del(blist[-1])
		elif char in [')', '}', ']']:  			# catches surplus closing brackets without openers.
			return False
			

	if not blist:
		return True		# an empty list is a clean queue!
	else:
		return False	# a non-empty list means surplus opening brackets.

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"((5+3)*2+1)") == True, "Simple"
    assert checkio(u"{[(3+1)+2]+}") == True, "Different types"
    assert checkio(u"(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio(u"[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio(u"(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio(u"2+3") == True, "No brackets, no problem"
    assert checkio(u"(((([[[{{{3}}}]]]]))))") == False, "Test 7"
    assert checkio(u"(((1+(1+1))))]") == False, "Test 11, bounds checker"