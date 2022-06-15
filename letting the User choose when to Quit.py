'''promt = "\nTell me something, and I will repeat it back to you: "
promt += "\nEnter 'quit' to end the program. "'''

'''message = ""
while message != 'quit':
    message = input(promt)
    if message != 'quit':
        print(message)
    print('\nGoodbye!')'''

'''active = True
while active:
    massage = input(promt)
    
    if massage == 'quit':
        active = False
    else:
        print(massage)'''

# using break to exit a loop

'''promt = "\nPlease enter the name of the city you want to visit: "
promt += "\n(Enter 'stop' when you are finished.) "

while True:
    city = input(promt)
    
    if city == 'stop':
        break
    else:
        print('I would love to go to ' +  city.title() + '!')'''

# using continue in a loop

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    
    print(current_number)