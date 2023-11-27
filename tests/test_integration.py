from lib.menu import Menu
from lib.order import Order
from unittest.mock import Mock

# add items in the list of menu with prices

def test_add_dish_with_price():
    menu = Menu()
    dish_1 = "pizza"
    dish_2 = "burger"
    price_1 = 10
    price_2 = 12
    menu.add_dishes_menu(dish_1, price_1)
    menu.add_dishes_menu(dish_2, price_2)
    assert menu.list_of_dishes () == [{"dish": "pizza", "price": 10}, {"dish": "burger", "price": 12}]
    
def test_ordering_one_dish_and_other_dish():
    menu = Menu()
    dish_1 = "pizza"
    dish_2 = "burger"
    price_1 = 10
    price_2 = 12
    menu.add_dishes_menu(dish_1, price_1)
    menu.add_dishes_menu(dish_2, price_2)
    menu.list_of_dishes () == [{"dish": "pizza", "price": 10}, {"dish": "burger", "price": 12}]
    order1 = Order("pizza", 10)
    order2 = Order ("burger", 12)
    order1.select_dish(1)
    order2.select_dish(2)
    assert order1.get_selected_dishes() == [{"dish": "pizza", "price": 10, "quantity": 1}]
    assert order2.get_selected_dishes() == [{"dish": "burger", "price": 12, "quantity": 2}]
    
def test_ordering_same_dish_twice_with_total_amount():
    menu = Menu()
    dish = "pizza"
    price = 10
    menu.add_dishes_menu(dish, price)
    assert menu.list_of_dishes () == [{"dish": "pizza", "price": 10}]
    order = Order("pizza", 10)
    order.selected_dishes("pizza", 10, 3)
    assert menu.total_price(order) == 30
    
