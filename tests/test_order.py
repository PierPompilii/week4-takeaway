from lib.order import Order

#selecting only one dish 

def test_ordering_only_one_dish():
    order = Order("pizza", 10)
    order.select_dish(1)
    assert order.get_selected_dishes() == [{"dish": "pizza", "price": 10, "quantity": 1}]
    
# select the same dish twice 

def test_ordering_two_dishes():
    order = Order("burger", 12)
    order.select_dish(2)
    assert order.get_selected_dishes() == [{"dish": "burger", "price": 12, "quantity": 2}]

    
