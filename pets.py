pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'dog' in pets:
    pets.remove('dog')
    pets.remove('cat')

print(pets)