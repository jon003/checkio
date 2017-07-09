#!/usr/bin/python
''' http://www.checkio.org/mission/hamming-distance2/solve/ ''' 

def tobin(number):
	a = format(number, '#012b')
	return a[2:]

print len(tobin(999999))
print len(tobin(1))

print len(format(999999, '#010b')[2:])

def checkio(n, m):
	results = 0
	n = tobin(n)
	m = tobin(m)

	for x in range(21):
		print n[x] + m[x]
		if n[x] != m[x]:
			results += 1 

	return results

#print checkio(1, 999999)
'''
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
'''