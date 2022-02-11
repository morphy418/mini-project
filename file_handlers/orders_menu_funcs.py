from file_handlers.file_management import deletion_confirmation, read_csv_file, write_csv_file, update_or_skip, deletion_confirmation
from file_handlers.fieldnames import order_fieldnames
from file_handlers.product_menu_funcs import print_products
from file_handlers.couriers_menu_funcs import print_couriers

def print_orders(database_list):
  for order in database_list:
    index = database_list.index(order)
    print(f'''
    Order ID: {index} 
    Customer: {order["customer_name"]} 
    Customer's address: {order["customer_address"]} 
    Customer's phone: {order["customer_phone"]}
    Courier: {order["selected_courier"]}
    Order status: {order["order_status"]}
    Order items: {order["order_items"]}''')

def create_order(database_list):
  orders_list = database_list

  customer_name = input("\nPlease add the customer's name: ")
  customer_address = input("\nPlease enter the customer's address: ")
  customer_phone = input("\nPlease enter the customer's phone: ")
  print_couriers(read_csv_file("data/couriers.csv"))
  while True:
    try:
      selected_courier = int(input("Please select from a the available couriers above by entering their ID: "))
    except ValueError as err:
      print("\nInvalid number. Please try again!")
    else:
      break  
  order_status = "preparing"
  print_products(read_csv_file("data/products.csv"))
  order_items = input("Please select multiple products seperated by comma: ").split(",")
  order_items_list = [int(item) for item in order_items]

  new_order = f'''
  New Order:
  Customer: {customer_name} 
  Customer's address: {customer_address} 
  Customer's phone: {customer_phone}
  Courier: {selected_courier}
  Order status: {order_status}
  Order items: {order_items_list}'''
  print(new_order)
  
  new_order_dict = {
    "customer_name": customer_name,
    "customer_address" : customer_address,
    "customer_phone" : customer_phone,
    "selected_courier" : selected_courier,
    "order_status" : order_status,
    "order_items" : order_items_list
    }

  orders_list.append(new_order_dict)

  write_csv_file("data/orders.csv", orders_list, order_fieldnames)

def update_order_status(database_list):
  orders_list = database_list
  print_orders(orders_list)

  while True:
    try:
      order_index = int(input("\nWhich order status would you like to update? Enter their ID number: "))
      print(f'\nOrder status to update: {orders_list[order_index]}')
    except ValueError as err:
      print("\nInvalid number. Please try again!")
    else:
      break

  while True:
    try:
      order_status_list = ["preparing", "on the way", "delivered", "cancelled"]
      for status in order_status_list:
        print(f'{order_status_list.index(status)} - {status}')
      status_index = int(input('\n Please choose an order status (enter their number): '))
    except ValueError as err:
      print("\nInvalid number. Please try again!")
    else:
      break

  print(orders_list[order_index]["order_status"])
  print(order_status_list[status_index])

  orders_list[order_index]["order_status"] = order_status_list[status_index]
  write_csv_file("data/orders.csv", orders_list, order_fieldnames)

def update_order(database_list):
  orders_list = database_list
  print_orders(orders_list)

  while True:
    try:
      order_index = int(input("\nWhich order status would you like to update? Enter their ID number: "))
      chosen_order = orders_list[order_index]
    except ValueError as ve:
      print("\nInvalid number. Please try again!")
    else:
      break
  
  print(f'\nOrder to update: {chosen_order}\n')

  print("Please enter the new order data. (Hit 'Enter' if you don't want to change it): \n")
  
  updated_customer_name = input("\nPlease add the customer's name: ")
  updated_customer_address = input("\nPlease enter the customer's address: ")
  updated_customer_phone = input("\nPlease enter the customer's phone: ")
  print_couriers(read_csv_file("data/couriers.csv"))
  while True:
    try:
      updated_selected_courier = int(input("\nPlease select from a the available couriers above by entering their ID: "))
    except ValueError as ve:
      print(ve.args[0])
      if ve.args[0] == "invalid literal for int() with base 10: ''":
        updated_selected_courier = None
        break
      print("\nInvalid number. Please try again!")
    else:
      break
  print_products(read_csv_file("data/products.csv"))
  updated_order_items = input("Please select multiple products seperated by comma: ").split(",")
  updated_order_items_list = [int(item) for item in updated_order_items]

    # order_status_list = ["preparing", "on the way", "delivered", "cancelled"]
    # for status in order_status_list:
    #   print(f'{order_status_list.index(status)} - {status}')
    # updated_status_index = int(input('\n Please choose an order status (enter their number)'))
    # updated_order_status = order_status_list[updated_status_index]

  updated_customer_obj = [
    updated_customer_name, 
    updated_customer_address, 
    updated_customer_phone, 
    updated_selected_courier,
    updated_order_items_list 
    # updated_order_status
    ]

  update_or_skip(order_fieldnames, updated_customer_obj,chosen_order)

  write_csv_file("data/orders.csv", orders_list, order_fieldnames)

def delete_order(database_list):
  orders_list = database_list
  print_orders(orders_list)
  
  while True:
    try:
      deletion_index = int(input("\nWhich order would you like to delete? Enter their ID number: "))
    except ValueError as ve:
      print("\nInvalid number. Please try again!")
    else:
      break

  deletion_confirmation(orders_list, deletion_index)

  write_csv_file("data/orders.csv", orders_list, order_fieldnames)

  