import spacy 

nlp = spacy.load("en_core_web_md")

#create a function that returns which movies a user would like to watch next given
# they have just watched PLANET HULK

# list of text to run similarity search on
last_watched_movie = [
    "Will he save their world or destroy it? When the hulk becomes too dangerous for the Earth, the illuninati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace.  Unfortunately, Hulk lands on the planet Sakaar where he is sold to slavery and trained as a gladiator."
]

# print("-------------Last watched movie similarity---------------")
for token in last_watched_movie:
    token = nlp(token)
    for token_ in last_watched_movie:
        token_ = nlp(token_)
        # print(token.similarity(token_))

#open file in read mode and return a list of movies to compare with last_watched_movie
with open("Python38/movies.txt", "r") as movie_option_file:
    movie_options = movie_option_file.readlines()
   
#create a list of movies to compare with last_watched_movie
for i in movie_options:
    # print(i.split("\n"))
    
    # print("-------------Movies similarity---------------")
    for token in movie_options:
        token = nlp(token)
        for token_ in movie_options:
            token_ = nlp(token_)
            # print(token.similarity(token_))
        
# Get the extent of similarity between the last_watched_movie and movie_options.
# loop through every movie in movie_options and compare it with last_watched.      

# print("-------------Movies & last_watched similarity---------------")
closely_matched_movies =[]
for token in movie_options:
    token = nlp(token)
    for token_ in last_watched_movie:
        token_ = nlp(token_)
        if token.similarity(token_) > 0.80:
            print(token.similarity(token_))
            closely_matched_movies.append(token.similarity(token_))
print(closely_matched_movies) 
print(max(closely_matched_movies))  

for i in closely_matched_movies:
    if i == max(closely_matched_movies):
        print(f"""
              
        Here is your most similar movie matched from your list of movies, 
        to watch next: {token}
        
        """)
            
            
            
           
        
        
#https://www.tutorialspoint.com/python/list_max.htm
#https://realpython.com/python-append/#:~:text=Python%20provides%20a%20method%20called,list%20using%20a%20for%20loop.
# https://www.w3schools.com/python/ref_string_join.asp