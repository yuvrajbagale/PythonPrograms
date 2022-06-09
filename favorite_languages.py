favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name, language in favorite_language.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
print('\n')
    
for x in favorite_language.keys():
    print(x.title())
    
print('\n')

friends = ['phil', 'sarah']
for i in favorite_language.keys():
    print(i.title())
    
    if i in friends:
        print(" Hi " + i.title() + ", I see your favorite language is " + favorite_language[i].title() + "!")
        
print('\n')

if 'yuvraj' not in favorite_language.keys():
    print('Yuvraj, Please take our poll!\n')
    
#Loping Through a Dictionary's Keys in order

for y in sorted(favorite_language.keys()):
    print(y.title() + ", thank you for taking the poll.\n")
    
# Looping Through All Values in a Dictionary

print("the following languages have been mentioned:\n")
for language in favorite_language.values():
    print(language.title())
print('\n\n')

print("the following languages have been mentioned:")
for language in set(favorite_language.values()):
    print(language.title())