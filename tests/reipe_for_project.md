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

class OrderMenu:
    def __init__(self):
        #parameters:
        #self.menu = {}

    
    def list_of_dishes(self):
        # return a list with all the dishes with prices 
        # for example {dish: pizza, price: 10}

    def select_dish(self):
        # Add the selected dish to the menu with a specified quantity
        # Parameters:
        # quantity: an int representing the number of dishes (default is 1)

    def total_amount(self):
        # return: total amount (sum) of selected dishes 
    
    def delivery_time(self, minutes):
        # Parameters:
        #minutes: an int representig time to deliver
        #return delivery time 

class Order:
    def __init__(self, dish, price)
    #parameters:
    #dish is a string representig a dish
    #price is a int associate to a dish 

    def time_to_make(self, minutes):
        #parameter 
        # minutes: is a int repsentig time 
        #return a int equivalent for time to make

3. Create Examples as Integration Tests

4. Create Examples as Unit Tests

5. Implement the Behaviour
