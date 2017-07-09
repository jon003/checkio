''' http://www.checkio.org/mission/simple-areas/solve/ '''

import math

def simple_areas(*args):
	if len(args) == 1:
		diameter = args[0]
		area = math.pi * (diameter / 2.0) ** 2
		return round(area, 2)
	if len(args) == 2:
		(length, width) = args
		area = float(length) * width
		return area
	if len(args) == 3:
		(a, b, c) = args
		a = float(a)
		p = (a + b + c)/2
		area = math.sqrt(p * ((p - a) * (p - b) * (p - c)))
		return area


def almost_equal(checked, correct, significant_digits=2):
    precision = 0.1 ** significant_digits
    return correct - precision < checked < correct + precision


print simple_areas(3)
print simple_areas(2, 2)
print simple_areas(2, 3)
print simple_areas(3, 5, 4)
print simple_areas(1.5, 2.5, 2)

'''
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(simple_areas(3), 7.07), "Circle"
    assert almost_equal(simple_areas(2, 2), 4), "Square"
    assert almost_equal(simple_areas(2, 3), 6), "Rectangle"
    assert almost_equal(simple_areas(3, 5, 4), 6), "Triangle"
    assert almost_equal(simple_areas(1.5, 2.5, 2), 1.5), "Small triangle"
'''