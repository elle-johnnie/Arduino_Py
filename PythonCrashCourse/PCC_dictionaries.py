# Python Crash Course
# Dictionary exercises

box_0 = {'color': 'green', 'points': 5}
print (box_0['color'])
new_points = box_0['points']
print ("There is an increase of " + str(new_points)+ " points!")
box_0['x_position'] = 0
box_0['y_position'] = 25
print box_0

box_1 = {}

box_1['color'] = 'blue'
box_1['points'] = 25

print box_1

print ("The box is " + box_1['color'] + ".")

box_1['color'] = 'red'

print ("The box is now " + box_1['color'] + ".")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print ("Original x_position: " + str(alien_0['x_position']))

alien_0['speed'] = 'fast'

# move alien to right
# determine how far to move alien based on current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # this must be a fast alien
    x_increment = 3

# the new position is the old position plus the increment based on speed
alien_0['x_position'] = alien_0['x_position'] + x_increment

print ('The new x_position is ' + str(alien_0['x_position']))

print alien_0

del alien_0['speed']

print alien_0

favorite_languages = {
    'ab' : 'python',
    'eve' : 'c',
    'rudy' : 'ruby',
    'elle' : 'python',
}

print ("Elle's favorite language is " +
       favorite_languages['elle'].title() +
       ".")

bridget_dic = {
    'first_name': 'bridget',
    'last_name': 'egan',
    'age': 39,
    'city': 'Portland',
    'sing': 'operas',
    'look': 'hermit crabs',
}
print ("print Bridget's dict")
print bridget_dic

print (bridget_dic['first_name'].title() +
       " lives in " + bridget_dic['city'].title() +
       " and is " + str(bridget_dic['age']) +
       " years old. " + bridget_dic['first_name'].title() +
       " likes to sing " + bridget_dic['sing'] +
       " and look  " + bridget_dic['look'] + ". \n")

print ("First name:" + '\n\t' + bridget_dic['first_name'].title() +
       "\n Last name:" + '\n\t' + bridget_dic['last_name'].title() +
       "\n Age:" + '\n\t' + str(bridget_dic['age']) +
       "\n City:" + '\n\t' + bridget_dic['city'])

for key, value in bridget_dic.items():
    print ("\nKey: " + key)
    print("Value: " + str(value))

for name, language in favorite_languages.items():
    print (name.title() + "'s favorite language is " +
           language.title() + ".")

for name in favorite_languages.keys():
    print(name.title())

friends = ['ab', 'elle']
for name in sorted(favorite_languages.keys()):
    print(name.title())

    if name in friends:
        print (" Hi " + name.title() +
               ". I see your favorite language is " +
               favorite_languages[name].title() + "!")
print ("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print ("-" * 20)

for language in set(favorite_languages.values()):
    print(language.title())








