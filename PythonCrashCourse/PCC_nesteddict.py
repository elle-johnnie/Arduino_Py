# Python Crash Course practice
# fun with nested dicts

# empty list storing all divisions - LIST OF DICTIONARIES
divisions = []

# 30 divisions
for division_number in range(30):
    new_division = {'color': 'blue', 'miles': 50, 'rate': 'slow'}
    divisions.append(new_division)

# modify division characteristics
for division in divisions[2:4]:
    if division['color']== 'blue':
        division['color'] = 'green'
        division['miles'] = 75
        division['rate'] = 'medium'

# display first 5 divisions
for division in divisions[:5]:
    print(division)
print("...")

# display total divisions created
print ("Total number of divisions created is: " + str(len(divisions)))

# LISTS IN A DICTIONARY = multiple values with a single key
preferred_languages = {
    'jose': ['python', 'ruby'],
    'yeti': ['c is for CHASE!'],
    'sattva' : ['cookies', 'chocolate'],
    'filson' : ['python', 'haskell'],
}

# read through all name keys in dictionary and print list of favorite
# programming  values associated
# with each key
for name, languages in preferred_languages.items():
    # determine if list of favorite languages holds more than one value
    if len(languages) > 1:
        print ('\n' + name.title() + "'s favorite languages are:")
        for language in languages:
            print('\t' + language.title())
    else: # return statement in singular format
        print ('\n' + name.title() + "'s favorite language is:")
        for language in languages:
            print('\t' + language.title())

# DICTIONARY WITHIN A DICTIONARY
users = {
    'ejohnson': {
        'first': 'elle',
        'last': 'johnson',
        'location': 'portland',
    },
    'began': {
        'first': 'bridgeeee',
        'last': 'egan',
        'location': 'beach',
    },
    'yboomba': {
        'first': 'yeti',
        'last': 'boombaletti',
        'location': 'playground',
    },
}
# loop throug users in dictionary, each key stored in value 'username'
# dictionary called 'user_info' associated with each usermame dictionary
for username, user_info in users.items():
    # return username and user_info
    print ("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print ('\tFull name: ' + full_name.title())
    print ('\tLocation: ' + location.title())



