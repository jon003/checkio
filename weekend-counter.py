''' http://www.checkio.org/mission/weekend-counter/solve/ '''

from datetime import timedelta, date


def daterange(start_date, end_date):
	# credit: http://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

def checkio(from_date, to_date):
	to_date = to_date + timedelta(days=1) # don't forget the last day!
	rest_day = 0
	for single_date in daterange(from_date, to_date):
		if single_date.weekday() == 5 or single_date.weekday() == 6:
			rest_day += 1
	return rest_day

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"
