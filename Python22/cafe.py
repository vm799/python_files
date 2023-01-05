# create a list for a cafe menu with at least 4 items
# create a dictionary called stock, should have stock value for each item
# create another dictionary called price with the prices for each item
# calculate and print the total stock worth in the cafe

cafe_menu_list = ["brownies", "cookies", "rockyroad", "muffins"]

stock = {
    "brownies": 12 , 
    "cookies": 24, 
    "rockyroad": 10, 
    "muffins": 8
    }

price = {
    "brownies": 1.25 , 
    "cookies": 0.80, 
    "rockyroad": 0.75, 
    "muffins": 1.15
    }

stock_values = stock.values() #return the values of the stock list

price_values = price.values()

total_stock_per_menu_item = []
for i1, i2 in zip(stock_values, price_values):  # for each item in each list use the zip() 
# function to multiply each element together
    total_stock_per_menu_item.append(i1*i2) # areturn the product (stock * price) of each list to new list

total_stock_worth = sum(total_stock_per_menu_item) #adding all together to get total stock worth
rounded_total_stock = round(total_stock_worth,2) # 2 dp
print(f"""
      
      The total stock worth in the cafe is: £{rounded_total_stock}
      
      """)


#https://www.w3schools.com/python/ref_func_round.asp
#https://www.entechin.com/how-to-multiply-two-lists-in-python/#:~:text=Multiply%20two%20lists%20using%20for%20loop,-We%20can%20simply&text=Through%20for%20loop%2C%20we%20can,of%202%20or%20more%20iterables.