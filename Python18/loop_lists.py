# define a slist of 5 favourite movies
# loop over the list to print out a statement for example Movie: {name of movie}
# try and find a way of labelling movie 1 with the firstmovies name
# use enumerate

print("""
      Challenge 1: 
      """)
my_favourite_movies =["wall-e", "hot fuzz", "dark knight", "gladiator", "pulp fiction" ]

for movie in my_favourite_movies:
    print(f"Movie: {movie}")
    
#https://realpython.com/python-enumerate/
# enumerate() function returns 2 loop variables - the count of the loop iteration and the 
# value of the item at that point of iteration

print("""
      Challenge 2: 
      """)

for count, movie in enumerate(my_favourite_movies, start=1): #start=1 to start movie count from 1
    print(f"Movie {count}: {movie}")