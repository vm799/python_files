# name 3 products user needs to buy
# request price of each product to 2dp
# add cost of all products
# calc average of all 3
# print out sentence


product1 = input("Please type in first item on your shopping list: ")
product2 = input("Please type in second item on your shopping list: ")
product3 = input("Please type in third item on your shopping list: ")

print(product1)
print(product2)
print(product3)

price_product1 = (input(f"Please type in the cost of the {product1} including pence to 2 decimal values: "))
price_product2 = (input(f"Please type in the cost of the {product2} including pence to 2 decimal values: "))
price_product3 = (input(f"Please type in the cost of the {product3} including pence to 2 decimal values: "))

print(price_product1)
print(price_product2)
print(price_product3)

total_price = float(price_product1) + float(price_product2) + float(price_product3)
print(total_price)

av_price =(total_price /3 )

# https://www.w3schools.com/python/ref_func_round.asp
print(round((av_price),2))

print(f"The Total of {product1}, {product2}, {product3} is £{total_price} and the average price of the items is £{av_price}.")
