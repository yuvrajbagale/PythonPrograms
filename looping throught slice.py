player_name = ['sachin','virat','dhoni','yuvraj','rohit','shikhar']
print("here are the players:")
for x in player_name:
    print(x.title())

#Copping a list    
my_foods = ['pizza','falafel','carrot cake']
frind_foods = my_foods[:]

print("my favorite foods are:")
print(my_foods)

print("\nmy frind favorite foods are:")
print(frind_foods)

my_foods.append('cannoli')
frind_foods.append('ice cream')

print("\nmy favorite foods are:")
print(my_foods)

print("\nmy frind favorite foods are:")
print(frind_foods)

movies = ["bahubali","raocha","dangal","kabali","kabali","kabali"]
my_movies = movies[:]

print("\nmy favorite movies are:")
print(movies)

print("\nmy frind favorite movies are:")
print(my_movies)

movies.append('Love story')
print("\nmy favorite movies are updated:")
print(movies)
