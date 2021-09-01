from datetime import *
from _typeshed import Self


class BikeRental:
    def __init__(self, stock= 0):
        self.stock = stock

    def displaystock(self):
        print("We have {} bikes in our stock".format(self.stock))
        return self.stock

    def rentBikeonhourlyBasis(self, n):
        if n<=0:
            print("Number of bikes should be positive")
        elif n> self.stock:
            print("Sorry we have only {} bikes in our stock".format(self.stock))
        else:
            now = datetime.datetime.now()
            print("You have rented {} bike(s) today at {} hours".format(n, now.hour))
            print("You will be charged at $5 per hour")
            print("We hope you enjoy our service")

            self.stock -= n
            return now
    
    def rentBikeonDailyBasis(self, n):
        if n <= 0:
            print("Number of bikes should be positive")
        elif n > self.stock:
            print("Sorry we have only {} bikes in our stock".format(self.stock))
        else:
            now = datetime.datetime.now()
            print("You have rented {} bike(s) today {} hours".format(n, now.hour))
            print("You will be charged at $100 for each day per bike")
            print("We hope you enjoy our service")

            self.stock -= n
            return now
    
    def rentBikeOnWeeklyBasis(self, n):
        """
        Rents a bike on weekly basis to a customer.
        """
        if n <= 0:
            print("Number of bikes should be positive!")
            return None

        elif n > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None        
        
        else:
            now = datetime.datetime.now()
            print("You have rented {} bike(s) on weekly basis today at {} hours.".format(n, now.hour))
            print("You will be charged $60 for each week per bike.")
            print("We hope that you enjoy our service.")
            self.stock -= n

            return now
    
    def returnBike(self, request):
        rentalTime, rentalBasis, numofBikes = request
        bill = 0

        if rentalTime and rentalBasis and numofBikes:
            self.stock += numofBikes
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime

            if rentalBasis == 1:
                bill = round(rentalPeriod.seconds / 3600)

            elif rentalBasis == 2:
                bill = round(rentalPeriod.days) * 20 * numofBikes

            elif rentalBasis == 3:
                bill == round(rentalPeriod.days/7)* 60 * numofBikes



            if (3 <= numofBikes <= 5):
                print("You are eligible for Family Rental promotion of 30'%' discount")
                bill = bill * 0.7


            print("Thanks for returning your bike. Hope you enjoyed our service")
            print("That would be ${}".format(bill))
            return bill
        else:
            print("Are you sure you need a bike with us?")
            return None




class Customer:

    def __init__(self):
        self.bikes = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0

    def requestbike(self):
        bikes = input("How many bikes would you like to rent?")
        try:
            bikes= int(bikes)
        except ValueError:
            print("Thats not a positive integer!")
            return -1

        if bikes < 1:
            print("Invalid Input")
            return -1
        else: 
            self.bikes = bikes
        return self.bikes

    def returnbike(self):
        if self.rentalBasis and self.rentalTime and self.bikes:
            return self.rentalTime, self.rentalBasis, self.bikes
        else:
            return 0,0,0