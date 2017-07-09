""" http://www.checkio.org/mission/ghosts-age/

After some experimenting, Nikola thinks he has discovered the law of ghostly opacity. 
On every birthday, a ghost's opacity is reduced by a number of units equal to its age 
when its age is a Fibonacci number (Read about this here) or increased by 1 if it is not.

For example:
A newborn ghost -- 10000 units of opacity.
1 year -- 10000 - 1 = 9999 (1 is a Fibonacci number).
2 year -- 9999 - 2 = 9997 (2 is a Fibonacci number).
3 year -- 9997 - 3 = 9994 (3 is a Fibonacci number).
4 year -- 9994 + 1 = 9995 (4 is not a Fibonacci number).
5 year -- 9995 - 5 = 9990 (5 is a Fibonacci number).
"""

def fibby(maxfib):
        fiblist = [0, 1]
        for i in range(maxfib):
                fiblist.append(fiblist[i] + fiblist[i + 1])
        return fiblist

FIBBONACI = fibby(20)  # enough to preload fibbonaci a bit over 10k

def checkio(opacity):
	current_opacity = 10000
	for age in range(10000):
		if age in FIBBONACI:
			current_opacity -= age
		else:
			current_opacity += 1

		if current_opacity == opacity:
			return age

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"
