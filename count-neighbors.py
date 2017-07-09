""" http://www.checkio.org/mission/count-neighbours/ """

NEIGHBORS = ((-1, -1), (-1, 0), (-1, 1), (0, -1),
             (0, 1), (1, -1), (1, 0), (1, 1))


def count_neighbours(grid, row, col):
	total = 0
	for position in NEIGHBORS:
		(row_offset, col_offset) = position 	
		x = row + row_offset
		y = col + col_offset
		if (0 <= x < len(grid) and 0 <= y < len(grid[x])):
			total += grid[x][y]
	return total


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(
        ((1, 0, 0, 1, 0),
         (0, 1, 0, 0, 0),
         (0, 0, 1, 0, 1),
         (1, 0, 0, 0, 0),
         (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"


"""
testgrid =	((1, 0, 0, 1, 0),
         	(0, 1, 0, 0, 0),
         	(0, 0, 1, 0, 1),
         	(1, 0, 0, 0, 0),
         	(0, 0, 1, 0, 0))

def get_grid_value(grid, row, col):
	return grid[row][col]

def traverse_grid(grid):
	print 'Raw Grid:'
	print grid
	for i in range(len(grid)):
		print 'row #: %d, %r' % (i, grid[i])
		for j in range(len(grid[0])):
			print 'Position %d, %d has value %d' % (i,j,grid[i][j])

def print_neighbors(grid, row, col):
	for position in NEIGHBORS:
		(row_offset, col_offset) = position 	
		x = row + row_offset
		y = col + col_offset
		value = 0
		total = 0

		if (0 <= x < len(grid) and 0 <= y < len(grid[x])):
			value = grid[x][y]
			total += value
		else:
			value = 'None'

		if value is not 'None':
			print 'x: %d, y: %d, value %d Exists' % (x, y, grid[x][y])
		else:
			print 'x: %d, y: %d, value %d Position Does not Exist' % (x, y, grid[x][y])


"""

