''' http://www.checkio.org/mission/find-sequence/ 
	given a martix with equidistance length and depth, find a given sequence of numbers in it.
	the sequence could be horizontally, vertical or diagonal (downwards only)

	the sequence is constrained as 4 or more matching digits.
'''

def columns(matrix):
	''' extracts a list of columns from the matrix '''
	cols = []
	for i in range(len(matrix)):
		cols.append([row[i] for row in matrix])
	return cols

def search_hori(matrix):
	for row in matrix:
		if has_digit_sequence(row):
			return True
	return False

def search_vert(matrix):
	for col in columns(matrix):
		if has_digit_sequence(col):
			return True
	return False

def has_digit_sequence(search_list):
    ''' search for 4 digit recurring sequence in list '''
    matches = 0
    match_num = search_list[0]
    for i in search_list:
        if i == match_num:
            matches += 1
            if matches >= 4:
                return True
        else:
            match_num = i
    return False

testmatrix = [[1, 2, 1, 1],
              [1, 1, 4, 1],
              [1, 3, 1, 6],
              [1, 7, 2, 5]]

test2 = [[7,1,4,1],
        [1,2,5,2],
        [3,4,1,3],
        [1,1,8,1]]

test3 = [
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5], 
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
        ]

def search_diag(matrix):
    diags = []
    for offset in range(len(matrix)):
        minors = [ row[i+offset] for i,row in enumerate(matrix) if 0 <= i+offset < len(row)]
        diags.append(minors)
    for row in diags:
        print row
    for row in diags:
        if has_digit_sequence(row):
            return True
    return False

print search_diag(test3)

def checkio(matrix):
    #replace this for solution
    if search_hori(matrix):
    	return True
    elif search_vert(matrix):
    	return True
    elif search_diag(matrix):
    	return True
    else:
    	return False

#print checkio(test3)

'''

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"

'''

