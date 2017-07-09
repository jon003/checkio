""" http://www.checkio.org/mission/weak-point/

The durability map is represented as a matrix with digits. Each number is the durability measurement for the cell. 
To find the weakest point we should find the weakest row and column. 
The weakest point is placed in the intersection of these rows and columns. 
Row (column) durability is a sum of cell durability in that row (column). 
You should find coordinates of the weakest point (row and column). The first row (column) is 0th row (column). 
If a section has several equal weak points, then choose the top left point.

Peseudocode:

Sum each row in sequence.  
Store the row # (location) of lowest sum.  
  (Only change this location if the row is LOWER than previous, to give us 'leftmost'
Sum each column in sequence.
Store the col # (location) of lowest sum.  
  (Only change this location if the col is LOWER than previous, to give us 'topmost'

testgrid = ([7, 2, 7, 2, 8],  
            [2, 9, 4, 1, 7],
            [3, 8, 6, 2, 4],
            [2, 5, 2, 9, 1],
            [6, 6, 5, 4, 5])


testgrid = ([7, 2, 4, 2, 8],
            [2, 8, 1, 1, 7],
            [3, 8, 6, 2, 4],
            [2, 5, 2, 9, 1],
            [6, 6, 5, 4, 5])
"""


def weak_point(matrix):
    ''' Check two lists, return list position of the smallest number in the list. '''
    rows = sum_rows(matrix)
    cols = sum_cols(matrix)
    weak_row_pos, weak_col_pos = 0, 0 # initialize to the first value in the row.
    weak_row_sum, weak_col_sum = 99, 99 # start them very high.
    for i, num in enumerate(rows):
        if num < weak_row_sum:
            weak_row_pos = i
            weak_row_sum = num
    for i, num in enumerate(cols):
        if num < weak_col_sum:
            weak_col_pos = i
            weak_col_sum = num
    return  weak_col_pos, weak_row_pos

def sum_rows(matrix):
    ''' Sums up the rows of a given matrix, returns a list of their values. '''
    total = []
    for column in range(len(matrix[0])):
        row_sum = 0
        for i in range(len(matrix)):  
            row_sum += matrix[i][column]
        total.append(row_sum)
    return total

def sum_cols(matrix):
    ''' Sums up the volums of a given matrix, returns a list of their values. '''
    total = []
    for row in range(len(matrix)):
        column_sum = 0
        for i in range(len(matrix[row])):
            column_sum += matrix[row][i]
        total.append(column_sum)
    return total

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(weak_point([[1]]), (list, tuple)), "The result should be a list or a tuple"
    assert list(weak_point([[7, 2, 7, 2, 8],
                            [2, 9, 4, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [3, 3], "Example"
    assert list(weak_point([[7, 2, 4, 2, 8],
                            [2, 8, 1, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [1, 2], "Two weak point"
    assert list(weak_point([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]])) == [0, 0], "Top left"


