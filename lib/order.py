class Order:
    
    def __init__(self, dish, price):
        self.selected_dishes = [{"dish": dish, "price": price, "quantity": 0}]

    def select_dish(self, quantity=1):
        if quantity > 0:
            self.selected_dishes[0]['quantity'] += quantity

    def get_selected_dishes(self):
        return self.selected_dishes
    
