user = {
    'yuvi':{
        'first': 'Yuvraj',
        'last': 'Bagale',
        'location': 'Pune',
        },
    'piu':{
        'first': 'Pooja',
        'last': 'Bagale',
        'location': 'Beed',
        },
}
for username, user_info in user.items():
    print('\nUsername: ' + username)
    full_name = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']
    
    print('\tFull name: ' + full_name.title())
    print('\tLocation: ' + location.title())