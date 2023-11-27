from lib.menu import Menu

#have an empty dict for out menu


def test_empty_menu():
    menu = Menu ()
    assert menu.list_of_dishes () == []
    
#total price for 2 diferent dishes

def test_total_amount_dishes():
    menu = Menu()
    dish_1 = "pizza"
    dish_2 = "burger"
    price_1 = 10
    price_2 = 12
    menu.add_dishes_menu(dish_1, price_1)
    menu.add_dishes_menu(dish_2, price_2)
    menu.list_of_dishes()
    assert menu.total_price() == 22 


