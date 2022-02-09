from app import update_order_status

def test_update_order_status():
  def mock_orders_menu():
    print("We returned to the Orders Menu")

  database_list = [
    {'customer_name': 'Max', 
    'customer_address': '23 Cate Ave', 
    'customer_phone': ' 234324324', 
    'selected_courier': '2', 
    'order_status': 'preparing'}, 
    {'customer_name': 'Alex', 
    'customer_address': ' 55 Irn Bru', 
    'customer_phone': ' 55665566', 
    'selected_courier': ' 2', 
    'order_status': ' preparing'}
    ]

  expected = [
    {'customer_name': 'Max', 
    'customer_address': '23 Cate Ave', 
    'customer_phone': ' 234324324', 
    'selected_courier': '2', 
    'order_status': 'cancelled'}, 
    {'customer_name': 'Alex', 
    'customer_address': ' 55 Irn Bru', 
    'customer_phone': ' 55665566', 
    'selected_courier': ' 2', 
    'order_status': ' preparing'}
    ]

  actual = update_order_status(database_list, mock_orders_menu)

  assert actual == expected
  print("test_update_order_status: Passed")

test_update_order_status()