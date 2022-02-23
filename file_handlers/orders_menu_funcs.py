from file_handlers.file_management import deletion_confirmation, read_csv_file, write_csv_file, update_or_skip, deletion_confirmation
from file_handlers.fieldnames import order_fieldnames, courier_fieldnames, product_fieldnames
from file_handlers.product_menu_funcs import print_products
from file_handlers.couriers_menu_funcs import print_couriers
from src.db.db import delete_order_from_db, insert_new_order_into_db, read_list_from_db, update_order_in_db, update_order_status_in_db
from prettytable import PrettyTable

def print_orders(orders_list):
  table = PrettyTable()
  for c in order_fieldnames:
    table.add_column(c, [])
  for dct in orders_list:
    table.add_row([dct.get(c, "") for c in order_fieldnames])
  print(table)

def print_chosen_order(item, fieldnames):
  table = PrettyTable()
  table.field_names = fieldnames
  table.add_row(item.values())
  print(table)

def create_order(orders_list):
  print_orders(orders_list)

  customer_name = input("\nPlease add the customer's name: ")
  customer_address = input("\nPlease enter the customer's address: ")
  customer_phone = input("\nPlease enter the customer's phone: ")
  print_couriers(read_list_from_db("couriers", courier_fieldnames))
  while True:
    try:
      selected_courier = int(input("Please select from a the available couriers above by entering their ID: "))
    except ValueError as err:
      print("\nInvalid number. Please try again!")
    else:
      break  
  order_status = "preparing"
  print_products(read_list_from_db("products", product_fieldnames))
  order_items = input("Please select multiple product IDs seperated by comma: ").split(",")
  order_items_list = [int(item) for item in order_items]
  
  new_order = {
    "customer_name": customer_name,
    "customer_address" : customer_address,
    "customer_phone" : customer_phone,
    "selected_courier" : selected_courier,
    "order_status" : order_status,
    "order_items" : order_items_list
    }

  insert_new_order_into_db(order_fieldnames, new_order)
  print_chosen_order(new_order, order_fieldnames[1:])
  print("New order has been created!")

def update_order_status(orders_list):
  print_orders(orders_list)

  while True:
    try:
      order_id = int(input("\nWhich order status would you like to update? Enter their ID number: "))
      for order in orders_list:
        if order["order_id"] == order_id:
          chosen_order = order
    except ValueError as err:
      print("\nInvalid number. Please try again!")
    else:
      break

  print_chosen_order(chosen_order, order_fieldnames)
  order_status_list = ["preparing", "on the way", "delivered", "cancelled"]
  for status in order_status_list:
    print(f'{order_status_list.index(status)} - {status}')
  while True:
    try:
      status_index = int(input('\nPlease choose an order status (enter their number): '))
    except ValueError as err:
      print("\nInvalid number. Please try again!")
    else:
      break

  new_status = order_status_list[status_index]
  update_order_status_in_db(new_status, order_id)
  print("Order status has been updated!")

def update_order(orders_list):
  print_orders(orders_list)

  while True:
    try:
      updated_order_id = int(input("\nWhich order would you like to update? Enter their ID number: "))
      chosen_order = []
      for order in orders_list:
        if order["order_id"] == updated_order_id:
          chosen_order.append(order)
    except ValueError as ve:
      print("\nInvalid number. Please try again!")
    else:
      break

  print_orders(chosen_order)

  print("Please enter the new order data. (Hit 'Enter' if you don't want to change it): \n")
  
  updated_customer_name = input("\nPlease add the customer's name: ")
  updated_customer_address = input("\nPlease enter the customer's address: ")
  updated_customer_phone = input("\nPlease enter the customer's phone: ")
  print_couriers(read_list_from_db("couriers", courier_fieldnames))

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
  print_products(read_list_from_db("products", product_fieldnames))

  updated_order_items = input("Please select multiple products seperated by comma: ").split(",")
  updated_order_items_list = [int(item) for item in updated_order_items]

  order_status_list = ["preparing", "on the way", "delivered", "cancelled"]
  for status in order_status_list:
    print(f'{order_status_list.index(status)} - {status}')
  updated_status_index = int(input('\n Please choose an order status (enter their number)'))
  updated_order_status = order_status_list[updated_status_index]

  updated_order = [
    updated_customer_name, 
    updated_customer_address, 
    updated_customer_phone, 
    updated_selected_courier,
    updated_order_status,
    updated_order_items_list 
    ]

  chosen_order_update_check = chosen_order[0]
  updated_order = update_or_skip(order_fieldnames, updated_order, chosen_order_update_check)
  update_order_in_db(order_fieldnames, updated_order, updated_order_id)
  
  print("Order has been updated!")
def delete_order(orders_list):
  print_orders(orders_list)
  
  while True:
    try:
      deletion_id = int(input("\nWhich order would you like to delete? Enter their ID number: "))
      chosen_order_to_delete = []
      for order in orders_list:
        if order["order_id"] == deletion_id:
          chosen_order_to_delete.append(order)
    except ValueError as ve:
      print("\nInvalid number. Please try again!")
    else:
      break

  order_deleted = deletion_confirmation(orders_list, deletion_id, "order")
  delete_order_from_db(deletion_id)
  print_orders(chosen_order_to_delete)
  print("Order has been deleted!")

  