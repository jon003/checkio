'''  http://www.checkio.org/mission/playfair-cipher/ '''

import string
import itertools

base_keytable = 'abcdefghijklmnopqrstuvwxyz0123456789'

def pairwise(iterable):
	" Borrowed from http://stackoverflow.com/questions/5389507/iterating-over-every-two-elements-in-a-list "
	a = iter(iterable)
	return itertools.izip(a, a)

def delete_dup_letters(text):
	uniques = ''
	for letter in text:
		if letter not in uniques:
			uniques = uniques + letter
	return uniques

def startgrid(text):
	# start a new 6x6 matrix, populate with the text.
	text = delete_dup_letters(text)
	matrix = []
	line = []
	for letter in text:
		if len(line) <= 5:
			line.append(letter)
		else:
			matrix.append(line)
			line = [letter]

	# since we only append when we hit 5, above, this appends any final, shorter, lines left over.
	if len(line) > 0:
		matrix.append(line) 
	return matrix

def fillgrid(matrix):
	# take an existing 6x6 matrix, fill in remaining positions.
	keytable = base_keytable
	for line in matrix:
		for letter in line:
			keytable = keytable.replace(letter, "")

	line_number = 0 
	while line_number <= 5:
		if matrix[line_number]:
			line = matrix[line_number] # suck in existing line.
		else:
			line = []
		if len(line) <= 5:
			fill = keytable[0]
			keytable = keytable[1:]
			line.append(fill)
			matrix[line_number] = line # export the line back into the matrix.
		else:
			line_number += 1
			# catch fetch the next line unless it exists, so create it.
			if len(matrix) <= line_number and line_number < 6:
				matrix.append([])
	return matrix


def prepare_text(message):	
	message = message.translate(None, string.punctuation)
	message = message.replace(' ', '')
	message = message.lower()

	# playfair requires an even number of digraphs, so we pad with 'z'
	if len(message) % 2 == 1:
		message = message + 'z'
	digraphs = []
	for a,b in pairwise(message):
		digraphs.append(a+b)
	return digraphs


def find_xy(alpha, matrix):
	v, h = 0, 0
	while v < 5:
		h = 0
		while h < 5:
			if matrix[v][h] == alpha:
				return v, h
			else:
				h += 1
		v += 1

plaintext = 'Fizz Buzz is x89 XX'
key = 'Check IO 10!'

grid = startgrid('checkio10')
grid = fillgrid(grid)
for line in grid:
	print line

def encode_rule1(matrix, a, b, row):
	''' 
	A and B are the positions of the first and second letters of a digraph.  Row is the same for both.
	'''
	crypt = ''
	if a < 5:
		crypt = crypt + matrix[row][a+1]
	else:
		crypt = crypt + matrix[row][0]
	if b < 5:
		crypt = crypt + matrix[row][b+1]
	else:
		crypt = crypt + matrix[row][0]
	return crypt

#print encode_rule1(grid, 1, 4, 0)

def encode_rule2(matrix, a, b, column):
	''' 
	A and B are the positions of the first and second letters of a digraph.  Column is the same for both.
	'''
	crypt = ''
	if a < 5:
		crypt = crypt + matrix[a+1][column]
	else:
		crypt = crypt + matrix[0][column]
	if b < 5:
		crypt = crypt + matrix[b+1][column]
	else:
		crypt = crypt + matrix[0][column]
	return crypt

#print encode_rule2(grid, 1, 5, 2)


def encode_rule3(digraph, matrix):
	pass


def encode(message, key):
	''' 
	Encoding rules:
	1.) The two letters of the digraph are considered to be the opposing 
		corners of a rectangle in the matrix (key table).  Note their position
		and apply the following 4 rules:
		A.) If the letters appear on the same row, replace with the letters 
			to the right of each, respectively. (wrap as needed)
		B.) If the letters appear on the same column, replace with the letters 
			below each, respectively. (wrap as needed)
		C.) If the letters are NOT on the same row/column, then replace them
			with the opposite corner of the rectangle formed by the original 
			pair of letters.  The first encrypted letter is on the same row
			as the first plaintext letter, the second encrypted letter on the 
			same row as the second plaintext letter.

	'''
	return message


def decode(secret_message, key):
    return secret_message

#print encode("Fizz Buzz is x89 XX.", "checkio101")

'''
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert encode("Fizz Buzz is x89 XX.", "checkio101") == 'do2y7mt22kry94y2y2', "Encode fizz buzz"
    assert decode("do2y7mt22kry94y2y2", "checkio101") == 'fizxzbuzzisx89xzxz', "Decode fizz buzz"
    assert encode("How are you?", "hello") == 'ea2imb1ht0', "Encode How are you"
    assert decode("ea2imb1ht0", "hello") == 'howareyouz', "Decode How are you"
    assert encode("My name is Alex!!!", "alexander") == 'i1dlkxjqlexn', "Encode Alex"
    assert decode("i1dlkxjqlexn", "alexander") == 'mynameisalex', "Decode Alex"
    assert encode("Who are you?", "human") == 'rnvftc1jd5', "Encode WHo"
    assert decode("rnvftc1jd5", "human") == 'whoareyouz', "Decode Who"
    assert encode("ATTACK AT DAWN", "general") == 'ewwektewhnua', "Encode attack"
    assert decode("ewwektewhnua", "general") == 'attackatdawn', "Decode attack"
'''