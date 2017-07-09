""" http://www.checkio.org/mission/cowsay/ """


""" Cowsay rules:
The cow is always the same, only quote changes.
Multiple spaces in a row are replaced by one space.
The top border consists of underscore characters. It starts from a single space and ends before the border column.
Each line of the quote consists of these parts: quote border(1), space(1), line(1-39), space(1), quote border(1).
If line is less than 40 characters, it will fit into one string. The string is quoted in <>.
If the line is greater than or equal to 40 characters, it should be split by these rules:
Max line size is 39 chars. If any spaces are in the line, split it by the rightmost space (this space is removed from text) otherwise take the first 39 characters.
After the split align all lines to same length by adding spaces at the end of each line.
First line borders: /\
Middle line borders: ||
Last line borders: \/
The bottom border consists of the minus sign. Has same length as top.
cowsay console program has strange behavior in certain cases, this cases will not be tested here.
"""

COW = r'''
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

def cowsay(text):
	if len(text) < 40:
		topline = '_' * (len(text) + 2)
		botline = '-' * (len(text) + 2)
		line1 = ' ' + topline + '\n'
		line2 = '< ' + text + ' >' + '\n'
		line3 =  ' ' + botline
		text = line1 + line2 + line3 + COW
		print text
		return text
	else:
		lines = reformat(text)


def reformat(text):
	""" Takes a string over 40 char, returns the newly formatted text and the number of lines 
		Returns: 	lines, a list of length-formatted strings representing lines to be printed
	"""
	lines = []
	linecount = 0
	for word in text.split():
		print 'Processing Word: %s' % word
		if not lines:			# catch initial empty line state
			lines.append(word)
			print 'Initial Line Started, word added: %s' % word
		elif len(lines[linecount]) + len(word) < 39:
			newline = lines[linecount] + ' ' + word
			print 'Found space, New line: %s, length now: %d, line number: %d' % (newline, len(newline), linecount)
			lines[linecount] = newline
		elif len(word) > 39:
			sys.exit('Words over 39 characters are not accepted')
		else:
			print 'Triggering new line creation sequence.'
			lines.append('')
			linecount += 1
			lines[linecount] = newline
	return lines


""" 
for each word in the original text
 check current line length
 if you have room, append the word.
 if you don't have room, 
   pad the old line to 39.
   start a new line, append the word.

"""

print reformat('thisisalong linetotest')
print reformat('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
#cowsay('Checkio rulezz')
#print COW


# TODO: use textwrap.wrap to re-wrap lines. and x.ljust(39) to re set the length to 39

"""


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    expected_cowsay_one_line = r'''
 ________________
< Checkio rulezz >
 ----------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
    expected_cowsay_two_lines = r'''
 ________________________________________
/ A                                      \
\ longtextwithonlyonespacetofittwolines. /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

    expected_cowsay_many_lines = r'''
 _________________________________________
/ Lorem ipsum dolor sit amet, consectetur \
| adipisicing elit, sed do eiusmod tempor |
| incididunt ut labore et dolore magna    |
\ aliqua.                                 /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

    cowsay_one_line = cowsay('Checkio rulezz')
    assert cowsay_one_line == expected_cowsay_one_line, 'Wrong answer:\n%s' % cowsay_one_line

    cowsay_two_lines = cowsay('A longtextwithonlyonespacetofittwolines.')
    assert cowsay_two_lines == expected_cowsay_two_lines, 'Wrong answer:\n%s' % cowsay_two_lines

    cowsay_many_lines = cowsay('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do '
                                'eiusmod tempor incididunt ut labore et dolore magna aliqua.')
    assert cowsay_many_lines == expected_cowsay_many_lines, 'Wrong answer:\n%s' % cowsay_many_lines


"""