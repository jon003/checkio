def checkio(first, second):
    matches = []
    for searchword in first.split(','):
    	print 'Matching: %s in %s' % (searchword, second)
        if searchword in second.split(','):
            matches.append(searchword)
    matches.sort()
    return ','.join(matches)

print checkio(u"mega,cloud,two,website,final", u"window,penguin,literature,network,fun,cloud,final,sausage")

#These "asserts" using only for self-checking and not necessary for auto-testing
#if __name__ == '__main__':
#    assert checkio(u"hello,world", u"hello,earth") == "hello", "Hello"
#    assert checkio(u"one,two,three", u"four,five,six") == "", "Too different"
#    assert checkio(u"one,two,three", u"four,five,one,two,six,three") == "one,three,two", "1 2 3"
#    assert checkio(u"mega,cloud,two,website,final", u"window,penguin,literature,network,fun,cloud,final,sausage") == "cloud,final"