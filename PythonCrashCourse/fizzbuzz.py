# fizzbuzz in Python 2.7
##
# I just heard about this at a local meetup - thought I'd give it a go.
# The rules:
# Write a program that prints the numbers from
# 1 to 100. But for multiples of three print Fizz instead of the number and for the multiples of five print
# Buzz. For numbers which are multiples of both three and five print FizzBuzz

# create empty list
nums = []

# append 1-100 as items in num list
for i in range(1, 101):
    nums.append(i)
# print unaltered list
print nums

print ('Begin fizzbuzz test... \n')

for i in nums:
    if i % 3 == 0 and i % 5 == 0:
        print ('fizzbuzz')
    elif i % 3 == 0:
        print ('fizz')
    elif i % 5 == 0:
        print ('buzz')
    else:
        print i

print ('fizzbuzz testing complete.')





