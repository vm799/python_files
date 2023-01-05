# 1. build a while loop that shows a count down from 20 to 0
# 2. Any loop that displays all even numbers from 1 and 20
# 3. create a loop that produces * increasing with 1 more on a new line
# 4. create a program that can find the GCD/HCF of 2 positive integers
#       ask user for a number
#       ask user for another number
#       both need to be positive
#       find the HCF of both



print("Challenge 1:")

count = 0

while count <= 20:
    print(20-count)
    count +=1
    

print("Challenge 2:")

for i in range(1,21):
    if (i % 2 == 0):
        print(i)


print("Challenge 3:")

star = "*" 

for i in range(1, 6): 
    print("*" * i)
   
   
   
print("Challenge 4:")
# help with GCD https://www.programiz.com/python-programming/examples/hcf

num1 = int(input("Please enter a positive number:  "))
num2 = int(input("Thank you, now please enter another positive number:  "))

if num1 > num2:  #find smallest of 2 numbers to decide on HCF
    lowest_num = num2
else:
    lowest_num = num1
    
 #for all numbers upto the smallest num find what goes into both num1 and num2

gcd = 0
for i in range(1, lowest_num+1):
    if (num1 % i == 0) and (num2 % i == 0):
       hcf = i
print(hcf)
print(f"The GCD of {num1} and {num2} is  {hcf}") 
        
       
     
       