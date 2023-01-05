# Help someone decide wha best to wear in the temperature of the day
# depending on temp is warmer than 20 degrees
#  if it is the weekend
#  if it's sunny

from socket import if_nameindex


is_temp_warmer_than_20 = True
is_it_the_weekend = True
is_it_sunny = True

if (input("Is it sunny outside today? (yes/no) ")) == "yes":
    is_it_sunny = True
    
else:
    is_it_sunny = False
    
# print(is_it_sunny)   
    


if (input("Is it the weekend yet? (yes/no) ")) == "yes":
    is_it_the_weekend = True
else:
    is_it_the_weekend = False
    
# print(is_it_the_weekend)  
    

if (input("Is it warmer than 20 degrees out today? (yes/no) ")) == "yes":
    is_temp_warmer_than_20 = True
else:
    is_temp_warmer_than_20 = False
    
# print(is_temp_warmer_than_20)  

# if (is_it_the_weekend == True):
    
#     lower_body_dress = "shorts"
# else:

if (is_temp_warmer_than_20 == False):
    upper_body_dress = "long-sleeved shirt" 
else:
    upper_body_dress = "short-sleeved shirt" 
    
if (is_it_the_weekend == True):
    lower_body_dress = "shorts"
else:
   lower_body_dress = "jeans"
    
if (is_it_sunny == True):
    outer_wear = "cap"
else:
    outer_wear = "raincoat"
    
print(f"For your outfit today, please wear a {upper_body_dress} and {lower_body_dress}, it would also be great if you could please wear a {outer_wear}. Perfect. Thank you!")