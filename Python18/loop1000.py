# with 2 lines of code write out all the numbers from 1 to 1000
# with added logic print out the numbers that are even

print("""
      Part 1:  
      """)

num=0 #intialise num

for num in range(1,1001): #upto but not including 1001
    print(num)
    
print("""
      Part 2:  
      """)

for num in range(1,1001):
    if num %2 == 0:
        print(num)