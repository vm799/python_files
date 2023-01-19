
class Car(object):
    
    def __init__(self, year, mpg, speed):
        self.year= year
        self.mpg= mpg
        self.speed= speed
        
    def accelerate(self):
        return self.speed + 20
            
    def brake(self):
        return self.speed - 20
    
myCar = Car(1900, 50, 90)

print(myCar.speed)    
    
myCar = Car(1900, 50, 90).accelerate()

print(myCar)  


class Cab:
    no= 2
    numpx=2
    
    def __init__(self, name, kilometres, locations, cab_fare, px):
        self.name = name
        self.kilometres = kilometres
        self.cab_fare= cab_fare
        self.locations =  locations
        self.cab_fare = cab_fare
        self.px = px
        Cab.no = Cab.no + 1
        Cab.numpx =+ px
        
        
    def RatePerKm(self):
        return self.cab_fare/self.kilometres
    
    @classmethod
    def noofcabs(cls):
        return cls.no
    
firstcab  = Cab("Ramesh", 80, ['Delhi', 'Noida'], 2200, 3)
secondcab = Cab("Suresh", 60, ['Gurgaon', 'Noida'], 1500, 1)
thirdcab  = Cab("Dave", 20, ['Gurgaon', 'Noida'], 680, 2)

print(firstcab.RatePerKm())

print(Cab.noofcabs())