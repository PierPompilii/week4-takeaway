class Menu:
    
    def __init__(self):
        self.menu = []

    def list_of_dishes(self):
        return self.menu
    
    def add_dishes_menu(self, dish, price):
        self.menu.append({"dish": dish, "price": price})

    def total_price(self):
        total = 0
        for item in self.menu:
            total += item["price"] 
        return total