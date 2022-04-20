class Movie:
    def __init__(self,name,hero,heroine,rating):
        self.name=name
        self.hero=hero
        self.heroine=heroine
        self.rating=rating

    def info(self):
        print('Movie Name:',self.name)
        print('Hero Name:',self.hero)
        print('Heroine Name:',self.heroine)
        print('Rating Name:',self.rating)
        print()

movies=[Movie('Bahubali','Prabhas','Anushka',99),
        Movie('Spider','Mahesh','rekul',25),
        Movie('Raavan','sharukh','Kajol',85),
        Movie('Maari','Dhanush','Kajol',100)]
for movie in movies:
    movie.info()