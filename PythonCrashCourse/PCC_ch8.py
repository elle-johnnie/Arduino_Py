def greet_user(username, usertype='amazing'):
    print 'hello, '+ username.title() + ' you are : ' + usertype.upper() + '.'

# greet_user('pickles', 'sour')
# greet_user('carrot', 'bland')
# greet_user(usertype='cold', username='ice')
# greet_user(username='smoothie')

def make_shirt(size='large', message='Python!'):
    print "A " + size + " shirt is ordered with the message: '" + message + "' printed across the front."

# make_shirt('small', "hello, world.")
# make_shirt(size='large', message='Hello, world!')
# make_shirt()


def get_name(first, last, middle=''):

    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()

# musician = get_name('john', 'hooker', 'lee')
# print musician
# musician = get_name('jimi', 'hendrix')
# print musician

def build_person(first, last, age=''):
    person = {'first': first, 'last': last}
    if age:
        person['age'] = age
    #return a dictionary of info about a person

    return person

# musician = build_person('jimi', 'hendrix', age=35)
# print musician
# print musician.keys()
# print musician.values()

def get_formatted_name(first, last):
    full_name = first + ' ' + last
    return full_name.title()

# while True:
#     print '\nTell me your name, please.'
#     print '\nenter q at any time to quit'
#     f_name =raw_input('First name: ')
#     if f_name == 'q':
#         break
#     l_name = raw_input('Last name: ')
#     if l_name == 'q':
#         break
#     full_name = get_formatted_name(f_name, l_name)
#     print '\nHello, ' + full_name + '!'

def build_album(artist, title, tracks=''):
    album = {'artist': artist, 'title':title}
    if tracks:
        album['tracks'] = tracks

    return album

# cd = build_album('jimi', 'hendrix', 14)
# print cd
# cd = build_album('woody', 'guthrie')
# print cd

# while True:
#     print 'Provide album info.'
#     print "Enter 'q' at any time to quit."
#     album_name = raw_input('Album name: ')
#     if album_name == 'q':
#         break
#
#     artist_name = raw_input("Artist's name: ")
#     if artist_name == 'q':
#         break
#
#     album_tracks = raw_input('# of tracks: ')
#     if album_tracks == 'q':
#         break
#
#     album_info = build_album(album_name, artist_name, album_tracks)
#     print album_info
#
# print album_info

def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title()
        print msg

# usernames = ['bridge', 'yeti', 'l']
# greet_users(usernames)

# start w/ designs to be printed
unprinted_designs = ['phone case', 'robot', 'dodecahedron']
completed_models = []

# simulate printing each design until none are left
# move each printed design to completed_models
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print ("Printing model: " + current_design)
#     completed_models.append(current_design)

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print('Printing model: ' + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print('\nThe following models have been printed: ')
    for completed_model in completed_models:
        print(completed_model)

# unprinted_designs = ['case', 'robot', "ball"]
# completed_models = []
# print_models(unprinted_designs[:], completed_models)
# show_completed_models(completed_models)
#
# print unprinted_designs
dogs = ['Yeti', 'Udo', 'Beezy', 'Yatzi']


def show_dogs(dogs):
    for dog in dogs:
        print dog
show_dogs(dogs)

i = 0
def make_great(dogs):
    i = 0
    for dog in dogs:
        print i
        dog[i] = 'the Great' + str(dog[i])
        i = + 1
make_great(dogs)