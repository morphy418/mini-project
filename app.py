from file_handlers.product_menu_funcs import *
from file_handlers.couriers_menu_funcs import *
from file_handlers.orders_menu_funcs import *
from file_handlers.designs import *
from src.db.db import read_list_from_db, read_list_from_orders_table
from file_handlers.fieldnames import *
from os import system
from pprint import pprint
from prettytable import PrettyTable

def main_menu(*args):
  system('clear')
  print("Welcome to".center(50))
  banner()

  user_input = input("""
  Main Menu Options:

  (1-Products Menu) 
  (2-Couriers Menu)
  (3-Orders Menu)
  (0-Exit App) 

  Please enter the corresponding number: """)

  try:
    system('clear')
    main_menu_func = main_menu_options[user_input]
    main_menu_func()
    
  except KeyError as ke:
    print(f'{ke} is an invalid number, please try again!')
    main_menu()

# PRODUCTS MENU
def products_menu():
  system('clear')
  products_list = read_list_from_db("products", product_fieldnames)
  write_csv_file("data/products.csv", products_list, product_fieldnames)

  banner()
  
  chosen_menu_option = input("""
  Products Menu Options:

  (1-Print Products) 
  (2-Create New Product) 
  (3-Update Product) 
  (4-Delete Product) 
  (0-Return to Main Menu)

  Please enter the menu option number: """)

  try:
    products_menu_func = products_menu_options[chosen_menu_option]
    products_menu_func(products_list)
    input("Press Enter to continue...")
    if chosen_menu_option != "0":
      products_menu() 
    
  except KeyError as ke:
    print(f'{ke} is an invalid number, please try again!')
    products_menu()
    system('clear')

# COURIER MENU
def couriers_menu():
  system('clear')
  couriers_list = read_list_from_db("couriers", courier_fieldnames)
  write_csv_file("data/couriers.csv", couriers_list, courier_fieldnames)

  banner()

  chosen_menu_option = input("""
  Couriers Menu Options:

  (1-Print Couriers) 
  (2-Create New Couriers) 
  (3-Update Courier) 
  (4-Delete Courier) 
  (0-Return to Main Menu)

  Please enter the menu option number: """)

  try:
    courier_menu_func = courier_menu_options[chosen_menu_option]
    courier_menu_func(couriers_list)
    input("Press Enter to continue...")
    if chosen_menu_option != "0":
      couriers_menu()
    
  except KeyError as ke:
    print(f'{ke} is an invalid number, please try again!')
    couriers_menu()
    system('clear')

# ORDERS MENU
def orders_menu():
  orders_list = read_list_from_orders_table(order_fieldnames)
  write_csv_file("data/orders.csv", orders_list, order_fieldnames)
  system('clear')

  banner()

  chosen_menu_option = input("""
  Orders Menu Options:

  (1-Print Orders) 
  (2-Create New Order) 
  (3-Update Order Status) 
  (4-Update Order)
  (5-Delete Order) 
  (0-Return to Main Menu)

  Please enter the menu option number: """)

  try:
    orders_menu_func = orders_menu_options[chosen_menu_option]
    orders_menu_func(orders_list)
    input("Press Enter to continue...")
    if chosen_menu_option != "0":
      orders_menu() 
    
  except KeyError as ke:
    print(f'{ke} is an invalid number, please try again!')
    orders_menu()
    system('clear')

# MENU OPTIONS
main_menu_options = {
  "1" : products_menu,
  "2" : couriers_menu,
  "3" : orders_menu,
  "0" : exit_app
}

products_menu_options = {
  "1" : print_products,
  "2" : create_new_product,
  "3" : update_product,
  "4" : delete_product,
  "0" : main_menu,
}

courier_menu_options = {
  "1" : print_couriers,
  "2" : create_courier,
  "3" : update_courier,
  "4" : delete_courier,
  "0" : main_menu,
}

orders_menu_options = {
  "1" : print_orders,
  "2" : create_order,
  "3" : update_order_status,
  "4" : update_order,
  "5" : delete_order,
  "0" : main_menu,
}

main_menu()


