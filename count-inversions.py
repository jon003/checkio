def count_inversion(sequence):
    """
        Count inversions in a sequence of numbers
    """
    inversions = 0
    for position in sequence:
    	if 
    		inversions += 1
    return inversions

print count_inversion((1, 2, 5, 3, 4, 7, 6))


"""

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion((99, -99)) == 1, "Two numbers"
    assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"


"""