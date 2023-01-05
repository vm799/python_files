#create 4 functions to determine hotel, plane, car and total holiday cost

def hotel_cost(nights):
    return nights * 100  # charged at £100 ppn
   
def plane_cost(city):
    flight_cost =0
    if city == 1:
        flight_cost = 350
    elif city ==2:
        flight_cost = 450
    elif city == 3:
        flight_cost = 550
    elif city == 4:
        flight_cost = 650
    elif city == 5:
        flight_cost = 850
    else:
        flight_cost = 1000  #any other city/location not mentioned in menu options
    return flight_cost

def car_rental(days):
    return days * 50 #£50 per day of car rental

def holiday_cost(nights, city, days):
    total_holiday_cost = hotel_cost(nights) + plane_cost(city) + car_rental(days)
    print(f"""
          
Thank you.
Here is the total cost of your holiday: £{total_holiday_cost}.

The breakdown of the cost is :-

Hotel costs:  £{hotel_cost(nights)}
Flight costs: £{plane_cost(city)}
Car rental:   £{car_rental(days)}
Total:        £{total_holiday_cost}
""")
nights = int(input("""
                   
To work out the total cost of your holiday, we need to ask you for some details:

How many nights would you like to stay in the hotel for?  """))
days = int(input("""
How many days would you like to hire the car for your trip?  """))
city = int(input("""
To decide the cost of your flight please type in the number of the city would you like to fly to:

1. London
2. Paris
3. Sydney
4. Rome
5. Barcelona
6. Any other location
"""))
holiday_cost(nights, city, days)