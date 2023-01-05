# create 3 variables
# compare first 2 to determine largest
# determine if first variable is even/odd
# sort the 3 variables from largest to smallest


num1 = 3400000
num2 = 110000
num3 = 1900

largest =0 

if num1 > num2:
    print(num1)
else:
    print(num2)
    
if (num1 % 2 == 0):
    print("Even")
else:
    print("Odd")
    
print("SOLUTION ONE: ")
num_largest = max(num1, num2, num3)
num_smallest =min(num1, num2, num3)
    
#print(num_largest)  
#print(num_smallest)   

# To find middle number, add them all up and take away the 
# largest and smallest to reveal the middle

num_middle = num1 + num2 + num3 - (num_smallest + num_largest)
#print(num_middle)
print(num_largest, num_middle, num_smallest) 


print("SOLUTION TWO Conditional statement method:")
if num_largest == num1 and num_smallest == num2:
    print(num1,num3, num2 )
elif num_largest == num1 and num_smallest == num3:
    print(num1,num2, num3 )
elif num_largest == num2 and num_smallest == num1:
    print(num2,num3, num1 )
elif num_largest == num2 and num_smallest == num3:
    print(num2,num1, num2 )
elif num_largest == num3 and num_smallest == num2:
    print(num3,num1, num2 )
elif num_largest == num3 and num_smallest == num1:
    print(num3, num2, num1 )



"""
print("SOLUTION TWO: ")
if num1 > num2 and num2 > num3:
        print(num1,num2,num3)
    
elif num1 > num2 and num3 > num2:
    print(num1,num3,num2)

elif num2 > num1 and num1 > num3:
    print(num2,num1,num3)

elif num2 > num1 and num3 > num1:
     print(num2,num3,num1)
    
elif num3 > num2 and num1 > num2: 
    print(num3,num1,num2)
    
#else num3 > num2 and num2 > num1: 
    print(num3,num2,num1)
    
else:
     print(num3,num1,num2)
    """

    