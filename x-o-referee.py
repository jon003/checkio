''' http://www.checkio.org/mission/x-o-referee/ 

pseudocode
 check x win
 check o win
 check d win

'''

def check_h(letter, grid):
	for row in grid:
		if row[0] == letter and row[1] == letter and row[2] == letter:
			return True
	return False

def check_v(letter, grid):
	for col in range(len(grid)):
		if grid[0][col] == letter and grid[1][col] == letter and grid[2][col] == letter:
			return True
	return False

def check_d(letter, grid):
	# top left to bot right
	if grid[0][0] == letter and grid[1][1] == letter and grid[2][2] == letter:
		return True
	elif grid[0][2] == letter and grid[1][1] == letter and grid[2][0] == letter:
		return True
	else:
		return False

def checkio(game_result):
	if check_h('X', game_result) or check_v('X', game_result) or check_d('X', game_result):
		return 'X'
	elif check_h('O', game_result) or check_v('O', game_result) or check_d('O', game_result):
		return 'O'
	else:
		return 'D'

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        u"XXX",
        u"XX.",
        u"XOO"]) == "X", "Xs wins"
    assert checkio([
        u"X.O",
        u"XX.",
        u"XOO"]) == "X", "Xs wins"
    assert checkio([
        u"OO.",
        u"XOX",
        u"XOX"]) == "O", "Os wins"
    assert checkio([
        u"OOX",
        u"XXO",
        u"OXX"]) == "D", "Draw"
    assert checkio([
        u"O.X",
        u"XX.",
        u"XOO"]) == "X", "Xs wins again"

