''' http://www.checkio.org/mission/speechmodule/ '''

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
	result = ''
	# case for hundreds.
	if number > 99:
		number = str(number)
		result += FIRST_TEN[int(number[0]) - 1]
		result += ' hundred '
		number = number[1:]
		number = int(number)
	# case for OTHER_TENS with no first_ten digit.
	if number <= 99 and number >= 20 and (number % 10 == 0):
		result += OTHER_TENS[number[0]]
		number = ''
	elif number <= 99 and number >= 20:
		result += OTHER_TENS[number[0]]
		result += ' '

	# case for 10-19
	elif number >= 10 and number <= 19:
		print 'Translating: %r' % number
		result += SECOND_TEN[number-10]
	# case for 1-9
	elif number >= 1 and number <=9:
		print 'Translating: %r' % number
		result += FIRST_TEN[number-1]
	else:
		'Uncaught number.  I should never trigger: %r' % number


	# whitespace strip routine here.
	return result


#print checkio(4)
#print checkio(10)
print checkio(90)
print checkio(100)
print checkio(133)


'''
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
'''