''' http://www.checkio.org/mission/gcd/ '''

''' algo:
	sort list, choose largest integer.
	find all divisors for largest integer, add to new list: divisors
	for each of the remaining numbers in the list, check divisors list, delete any not divisors of new number.
'''

def div(integer, divisor):
	if integer % divisor == 0:
		return True
	else:
		return False

def greatest_common_divisor(*args):
	args = list(args)
	divisors = []
	integer_list = sorted(args)
	(integer_list, largest) = (args[:-1], args[-1])
	print integer_list, largest
	for x in range(largest):
		if div(largest, x):
			divisors.append(x)
	print 'max divisor list: %r' % divisors

	return divisors

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert greatest_common_divisor(6, 4) == 2, "Simple"
    assert greatest_common_divisor(2, 4, 8) == 2, "Three arguments"
    assert greatest_common_divisor(2, 3, 5, 7, 11) == 1, "Prime numbers"
    assert greatest_common_divisor(3, 9, 3, 9) == 3, "Repeating arguments"

