# calculate the cost of sending a parcel
# ask sender the price of package they would like to buy
# ask for the total distance of delivery in km
# final cost of package is delivery cost plus product cost
# 4 categories 
#   Air, insurance, gift, priority delivery

distance = 0

price_package = float(input("Please type in the price of the package you would like to buy: "))
#print(price_package)

distance= int(input("Please type in the total distance of the delivery (kilometres): "))
#print(price_package)

insurance = input("Please choose if you would like the limited insurance or full insurance please: (limited/full) ")
#print(distance)

gift = input("Please let us know if this is a gift: (True/False) ")
#print(distance)

delivery = input("Would you like the delivery to be standard or priority?: (standard/priority) ")
#print(distance)

transport = input("Please let us know if you would like the parcel to travel by air or freight? :  (air/freight) ")
#print(distance)

if(transport== "air"):
    distance_cost = 0.36*distance 
else:
    distance_cost = 0.25*distance

if insurance == "full":
    insurance_cost = 50
else:
    insurance_cost  = 25

if(gift == "True"):
    gift_added = 15
else:
    gift_added = 0
    
if(delivery == "priority"):
    delivery_added = 100
else:
    delivery_added= 20
    
    
    

total_cost_of_package = price_package + distance_cost + insurance_cost + gift_added + delivery_added
print(f"Total cost for this package is: R{total_cost_of_package}")
