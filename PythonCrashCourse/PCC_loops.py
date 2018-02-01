# Python Crash Course
# fun with loops

habitats = ["marine", "freshwater", "forest", "desert", "grassland", "swamp"]

for habitat in habitats:
    print ('\t' + habitat.title())


for value in range(0,51, 1):
    print value

numbers = list(range(0,21,5))
print numbers

squares = []
for value in range (1,11):
    #square = value**2
    squares.append(value**2)
print squares

print min(squares)
print max(squares)
print sum(squares)

squaresToo = [value**2 for value in range(1,11)]
print squaresToo

cubesToo = [value**3 for value in range(1,50)]
print cubesToo

print cubesToo[0:10]

for cube in cubesToo[:3]:
    print cube

foods = ['burger', 'apple', 'celery', 'tomato']
your_foods = foods[:]

print foods
print your_foods
foods.append('cake')
your_foods.append('potatoes')

print foods
print your_foods

print ('\n play with sorting function and method \n')
print ('forward')
print sorted(foods)
print ('reverse')
your_foods.sort(reverse=True)
print your_foods



