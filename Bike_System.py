
# Creating a CLASS which Holding Available Bike_Stock Number
class Bikeshop:
    def __init__(self,bike_stock):
        self.bike_stock = bike_stock

# Creating New Fuction which Display Available bike stock

    def display_bike_stock(self):
        print("Display Available Bikes ::" , self.bike_stock)

    def rent(self , bike_quntity):
        if bike_quntity <= 0:
            print("opps.. please Enter valid quntity")

        elif bike_quntity > self.bike_stock:
            print("please enter quntity in Available stock ")
            print("Available Bike_Stock is ::" , self.bike_stock)

        else:
            self.bike_stock = self.bike_stock - bike_quntity
            print("Available Bike_Stock is ::" , self.bike_stock)
            print(" Total Price of Bikes is ::" , bike_quntity * 100)

while True:
    obj = Bikeshop(200)
    user_take = int(input ( ''' Select One Number From below :
                
                1 Display total Bikes
                2 Total Rent of Bikes
                3 Available Colors
                4 Exit
                
                Enter Your Number :
                '''))

    print("Your Number is :" ,  user_take)

    if user_take == 1 :
        obj.display_bike_stock()

    elif user_take == 2:
        enter_quntity = int(input("Enter Quntity"))
        obj.rent(enter_quntity)
    elif user_take == 3:
        print('''Available colors are :
                1 RED
                2 BLACK
                3 BLUE
                4 WHITE''')
    else:
        break;