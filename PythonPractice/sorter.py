sample = [3,4,1,2,5,6]
#['m', 'k', 'L', 'A', 'z', 'a']

indA = 0

for char in sample:
    indB = indA + 1
    print char
    print indA
    print indB

    if char[indA] < char[indB]:
        char[indA], char[indB] = char[indB], char[indA]
        indA += 1
    else:
        indA += 1


print sample

