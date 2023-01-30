
import spacy 

nlp = spacy.load("en_core_web_md")

#create a function that returns which movies a user would like to watch next given
# they have just watched PLANET HULK

# list of text to run similarity search on
last_watched_movie = [
    "Planet Hulk: Will he save their world or destroy it? When the hulk becomes too dangerous for the Earth, the illuninati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace.  Unfortunately, Hulk lands on the planet Sakaar where he is sold to slavery and trained as a gladiator."
]

#open file in read mode and return a list of movies to compare with last_watched_movie
with open("Python38/movies.txt", "r") as movie_option_file:
    movie_options = movie_option_file.readlines()
        
# Get the extent of similarity between the last_watched_movie and movie_options.
# loop through every movie in movie_options and compare it with last_watched.      


#("-------------Movies & last_watched similarity---------------")
closely_matched_movies =[]

def next_movie_recommendation(movies, last_movie):
    
    #iterating through each movie in the movie options
    for token in movies:
        token = nlp(token)
        
        #and through the last_movie string
        for token_ in last_movie:
            token_ = nlp(token_)
            
            #add all similarity indexes to a list
            best_matched_movies = (token.similarity(token_), token)
            closely_matched_movies.append(best_matched_movies)

    #find the film with highest similarity index and print
    best_next_movie = max(closely_matched_movies)
    
    #remove the index from the tuple
    movie = best_next_movie[1]

    #slice the tuple to print the title and contents
    print(f"""

#-----------------------------------------------------------------#
    
Here is your most similar movie matched from your list of movies.
         
--**--Watch next--**--
        
        
**   {movie[0:2]}   **


--**--What is it about?--**--

{movie[3:]}
        
#------------------------------------------------------------------#

        """)
    

next_movie_recommendation(movie_options, last_watched_movie)          
            
            

#https://www.tutorialspoint.com/python/list_max.htm
#https://realpython.com/python-append/#:~:text=Python%20provides%20a%20method%20called,list%20using%20a%20for%20loop.
# https://www.w3schools.com/python/ref_string_join.asp