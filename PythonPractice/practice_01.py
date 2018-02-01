# Python 2.7
# write a function that adds 2 integers

def add2ints(a, b):
    result = a + b
    print result
    return result

add2ints(5, 6)

# count down from 5 to 0 in increments of one

print '\n'*2
for i in range(5, -1, -1):
    print i
    if i == 0:
        print ('Done!')
    else:
        print ('Counting Down!')