# Build a program to test if a string is a palindrome
# If it is then when the string is read from the start it is the same read backwards
# ask for an input by user
# test for a palindrome and return the relevant statements


print("""
      This program tests if your word is indeed a palindrome!
      """
      )
user_word = input("OK, go ahead and please type in a word that you would like to check:  ")
#print(user_word)

if (user_word==user_word[::-1]):  #if same as reversed 
    print(f"""
          Hurray {user_word}
          is a PALINDROME! 
          Who-hoo!
          """)
else:
    print(f"""
          oh no,  
          {user_word} is not a palindrome.
          """)



