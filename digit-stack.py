''' http://www.checkio.org/mission/digit-stack/solve/ '''

def digit_stack(commands):
    stack = []
    sum = 0
    for instruction in commands:
    	if instruction == 'POP':
    		# POP: add to sum, and take it off the stack
    		if len(stack) == 0:
    			pass
    		else:
	    		sum += int(stack.pop())
    	elif instruction == 'PEEK':
    		# PEEK: add to sum, but don't take it off the stack
    		if len(stack) != 0:
	    		sum += int(stack[-1])
    	else:
    		# PUSH: add to stack, don't change sum.
    		(push, value) = instruction.split()
    		stack.append(value)
    return sum

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8, "Example"
    assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
    assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
    assert digit_stack([]) == 0, "Nothing"

