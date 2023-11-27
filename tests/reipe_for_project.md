```python 
1. Describe the Problem

#As a customer
#So that I can check if I want to order something
#I would like to see a list of dishes with prices.

#As a customer
#So that I can order the meal I want
#I would like to be able to select some number of several available dishes.

#As a customer
#So that I can verify that my order is correct
#I would like to see an itemised receipt with a grand total.

#Use the twilio-python package to implement this next one. You will need to use mocks too.

#As a customer
#So that I am reassured that my order will be delivered on time
#I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.

2. Design the Class System

class Menu:
    def __init__(self):
        #parameters:
        #self.menu = {}

    
    def list_of_dishes(self):
        # return a list with all the dishes with prices 
        # for example {dish: pizza, price: 10}

    def select_dish(self, quantity):
        # Add the selected dish to the menu with a specified quantity
        # Parameters:
        # quantity: an int representing the number of dishes (default is 1)

    def total_amount(self):
        # return: total amount (sum) of selected dishes 
    
   

class Order:
    def __init__(self, dish, price)
    #parameters:
    #dish is a string representig a dish
    #price is a int associate to a dish 

    def select_dish(self, quantity):
        # Add the selected dish to the menu with a specified quantity
        # Parameters:
        # quantity: an int representing the number of dishes (default is 1)

    
class Takeaway

def time_to_make(self, minutes):
        #parameter 
        # minutes: is a int repsentig time 
        #return a int equivalent for time to make

 def delivery_time(self, minutes):
        # Parameters:
        #minutes: an int representig time to deliver
        #return delivery time 

3. Create Examples as Integration Tests

given menu 
i would like to see the dishes availables with the prices

def test_see_list_dishes_with_prices():
    order_menu = OrderMenu()
    dish_1 = Order ("pizza": 10)
    dish_2 = Order ("nuggets": 8)
    dish_3 = Order ("burger": 12)
    order_menu.list_of_dishes() #=> ["pizza": 10,"nuggests": 8, "burger": 12) 

given the list of dishes
i would like to select the dishes 

def test_quantity_of_dishes():
    order_menu = OrderMenu()
    dish_1 = Order ("pizza": 3)
    dish_2 = Order ("nuggets": 1)
    order_menu.select_dish() #=> ["pizza": 3, "nuggets": 1]

given the dishes selected
i want to know the price of the dishes selected

def test_price_dishes_selected ():
    order_menu = OrderMenu()
    order_menu.list_of_dishes = ["pizza": 10,"nuggests": 8, "burger": 12]
    order_menu.select_dish("pizza": 3)
    order_menu.selec_dish("nuggets": 1)
    order_menu.total_amount() #=> 38
    

4. Create Examples as Unit Tests

5. Implement the Behaviour
