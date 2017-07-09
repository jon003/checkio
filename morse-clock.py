''' http://www.checkio.org/mission/morse-clock/solve/ '''

''' this is not really a morse clock, but a binary clock. '''


def checkio(time_string):
	md = {'0': '....', '1': '.-', '2': '.-', '3': '.--', '4': '-..',  
		  '5': '.-.', '6': '..-', '7': '.---', '8': '.---', '9': '-..-'
	 	 }

	hours, minutes, seconds = time_string.split(:)
	
	for int in range(10):
		lookup = str(int)
		print 'converting occurances of %s to %s' % (lookup, md[lookup])
		time_string = time_string.replace(lookup, md[lookup])
		time_string = time_string.replace(':', ' # ')

	return time_string


print checkio(u"10:37:49")
print ".- .... : .-- .--- : -.. -..-"

'''
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio(u"21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio(u"00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio(u"23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"

'''
