# The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive).
# The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection
# search, the computer will guess the user's secret number!
# edX wk 2 Algorithms
# solution attempt 01/31/2018 @LJohnson

low = 0
high = 100
number = False

print('Think of a number between 0 and 100.')

while not number:
    mid = (high + low)//2
    print('Is your number %d ?' % mid)
    userinput = input('''Enter 'h' to indicate the guess is too high. 
                         Enter 'l' to indicate the guess is too low. 
                         Enter 'c' to indicate I guessed correctly.''')
    if userinput == 'l':
        low = mid

    elif userinput == 'h':
        high = mid

    elif userinput == 'c':
        print('Awesome I guessed your number correctly!')
        number = True

    else:
        print('Sorry I did not understand your response.')
