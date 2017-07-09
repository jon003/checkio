
def is_pal(text):
    if text == text[::-1]:
      return True
    else:
      return False

def substrings(input_string):
    l = len(input_string)
    result = [input_string[i:j+1] for i in xrange(l) for j in xrange(i,l)]
    return sorted(result, key=len, reverse=True)

def longest_palindromic(text):
    s = substrings(text)
    for test in s:
      if is_pal(test):
        return test

if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"

