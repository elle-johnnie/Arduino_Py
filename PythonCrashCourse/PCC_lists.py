# Python Crash Course
# exercises with lists
motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles[0] = 'ducati'

print motorcycles

motorcycles.append('honda')
print motorcycles

motorcycles.insert(1, 'harley')

del motorcycles[1]
print motorcycles

motorcycles.extend(['harley', 'vespa'])
print motorcycles

motorcycles_popped = motorcycles.pop()
print motorcycles
print ("The last bike I bought was a " + motorcycles_popped.title() + '.')

first_owned = motorcycles.pop(0)
print ("The first bike I bought was a " + first_owned.title() + '.')

motorcycles.remove('honda')
print motorcycles

motorcycles.extend(['honda', 'vespa', 'junker'])
print motorcycles

motorcycles.extend(['honda', 'vespa'])
print motorcycles

motorcycles.remove('honda')
print motorcycles

motorcycles.insert(5, 'a rusted out POS')
print motorcycles

#hard change to list via sort()
motorcycles.sort()
print motorcycles

motorcycles.sort(reverse=True)
print motorcycles

#temp change to list via sorted()
print (sorted(motorcycles))
motorcycles.reverse()
print motorcycles



