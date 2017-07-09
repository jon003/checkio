''' http://www.checkio.org/mission/triangle-angles/ '''

# law of consines based solution, input are in ascending order.

import math

def is_triangle(a, b, c):
	if a + b > c and a + c > b and b + c > a:
		return True
	else:
		return False

def find_angle(a, b, c):
	return int(round(math.degrees(math.acos((a * a + b * b - c * c)/(2.0 * b * c)))))
#	return round(math.degrees(math.acos((a * a + b * b - c * c)/(2.0 * b * c))))
#	return math.degrees(math.cos((a * a + b * b - c * c)/(2.0 * b * c)))
#								 ((4 * 4 + 5 * 5 - 3 * 3)/(2.0 * 5 * 3)))


def checkio(a, b, c):
	if is_triangle(a, b, c):
		a_angle = find_angle(a, b, c)
		b_angle = find_angle(c, b, a)
		c_angle = 180 - (a_angle + b_angle)
		return a_angle, b_angle, c_angle
	else:
		return 0, 0, 0


print find_angle(3, 4, 5)
print find_angle(4, 5, 3)
print find_angle(5, 4, 3)

#print checkio(4, 4, 4)
#print checkio(3, 4, 5)
#print checkio(0, 0, 0)


'''
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"

'''