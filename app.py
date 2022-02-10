from logging.handlers import RotatingFileHandler
from os import system
import csv
import pprint as pp

# FIELDNAMES

order_fieldnames = [
      "customer_name", 
      "customer_address", 
      "customer_phone", 
      "selected_courier", 
      "order_status", 
      "order_items"
      ]

product_fieldnames = [
      "product_name", 
      "product_type", 
      "product_price", 
      ]

courier_fieldnames = [
      "courier_name", 
      "courier_company", 
      "courier_phone", 
      "courier_availability",
      ]

# DESIGN

def banner():
  print("""
 ██████╗ █████╗ ███████╗███████╗    ██╗  ██╗██████╗ 
██╔════╝██╔══██╗██╔════╝██╔════╝    ██║  ██║╚════██╗
██║     ███████║█████╗  █████╗      ███████║ █████╔╝
██║     ██╔══██║██╔══╝  ██╔══╝      ╚════██║██╔═══╝ 
╚██████╗██║  ██║██║     ███████╗         ██║███████╗
 ╚═════╝╚═╝  ╚═╝╚═╝     ╚══════╝         ╚═╝╚══════╝!""")

# FILE MANAGEMENT

# def read_file(file_name):
#   with open(file_name, "r") as open_file:
#     file_contents = open_file.readlines()
#     return file_contents

# def write_file(file_name, list):
#   with open(file_name, "w") as database_file:
#     for item in list:
#       database_file.write(item.strip() + '\n')

# def generate_list_from_database(database):
#   with open(database, 'r') as data_file:
#     data = data_file.readlines()
#     data_list = [item.strip() for item in data]
#   return data_list

def read_csv_file(file_name):
  with open(file_name, "r", newline='') as database_file:
    reader = csv.DictReader(database_file)
    data = []
    for item in reader:
      data.append(item)
    return data

def write_csv_file(file_name, list, fieldnames):
  with open(file_name, "w", newline='') as database_file:
    writer = csv.DictWriter(database_file, fieldnames=fieldnames)
    writer.writeheader()
    for dict_item in list:
      # print(dict_item)
      writer.writerow(dict_item)

def update_or_skip(fieldnames, update_object, chosen_item):
  for update in update_object:
    if update != "" and update != None:
      index = update_object.index(update)
      chosen_item[fieldnames[index]] = update_object[index]

#MAIN MENU OPTIONS
def exit_app():
  print("\nYou exited the app.")
  print('''
                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ "$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
"$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  """$$$
   "$$$""""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$o
   o$$"   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$""$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  o$$$$$$$$$$$$$$$$$
  $$$$$$$$"$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$""""""""
 """"       $$$$    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$"      o$$$
            "$$$o     """$$$$$$$$$$$$$$$$$$"$$"         $$$
              $$$o          "$$""$$$$$$""""           o$$$
               $$$$o                                o$$$"
                "$$$$o      o$$$$$$o"$$$$o        o$$$$
                  "$$$$$oo     ""$$$$o$$$$$o   o$$$$""
                     ""$$$$$oooo  "$$$o$$$$$$$$$"""
                        ""$$$$$$$oo $$$$$$$$$$
                                """"$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$"
                                      "$$$""""
                                      
██╗  ██╗ █████╗ ██╗   ██╗███████╗     █████╗                 
██║  ██║██╔══██╗██║   ██║██╔════╝    ██╔══██╗                
███████║███████║██║   ██║█████╗      ███████║                
██╔══██║██╔══██║╚██╗ ██╔╝██╔══╝      ██╔══██║                
██║  ██║██║  ██║ ╚████╔╝ ███████╗    ██║  ██║                
╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝    ╚═╝  ╚═╝                
                                                             
███╗   ██╗██╗ ██████╗███████╗    ██████╗  █████╗ ██╗   ██╗██╗
████╗  ██║██║██╔════╝██╔════╝    ██╔══██╗██╔══██╗╚██╗ ██╔╝██║
██╔██╗ ██║██║██║     █████╗      ██║  ██║███████║ ╚████╔╝ ██║
██║╚██╗██║██║██║     ██╔══╝      ██║  ██║██╔══██║  ╚██╔╝  ╚═╝
██║ ╚████║██║╚██████╗███████╗    ██████╔╝██║  ██║   ██║   ██╗
╚═╝  ╚═══╝╚═╝ ╚═════╝╚══════╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝
                                                             ''')

# PRODUCT MENU OPTIONS

def print_products(database_list):
  for product in database_list:
    index = database_list.index(product)
    print(f'''
    Product ID: {index} 
    Name: {product["product_name"]} 
    Type: {product["product_type"]} 
    Price: {product["product_price"]}''')
  
def create_new_product(database_list):
  products_list = database_list

  new_product_name = input("\nPlease add a New Product: ")
  new_product_type = input("\nPlease enter the type of the new product: ")
  while True: 
    try:
      new_product_price = float(input("\nPlease enter the price of the new product: "))
    except ValueError as err:
      print("\nInvalid number. Please try again!")
    else:
      break

  new_product = {
    "product_name" : new_product_name, 
    "product_type" : new_product_type, 
    "product_price" : new_product_price
  }
  
  products_list.append(new_product)

  write_csv_file("data/products.csv", products_list, product_fieldnames)
  
  system('clear')
  
def update_product(database_list):
  products_list = database_list
  print_products(products_list)

  while True:
    try:
      update_index = int(input("\nWhich product would you like to update? Enter their ID number: "))
      chosen_product = products_list[update_index]   
    except ValueError as err:
      print("\nInvalid number. Please try again!")
    else:
      system('clear')
      break

  print(f'\Product to update: {chosen_product}\n')

  print("Please enter the new product data. (Hit 'Enter' if you don't want to change it): \n")

  updated_product_name = input("Updated Product Name: ")
  updated_product_type = input("Updated Product Type: ")
  while True:
    try:
      updated_product_price = float(input("Updated Product Price: "))
    except ValueError as ve:
      print("\nInvalid number. Please try again!")
    else:
      break

  updated_product_obj = [
    updated_product_name, 
    updated_product_type, 
    updated_product_price
  ]

  update_or_skip(product_fieldnames, updated_product_obj, chosen_product)

  write_csv_file("data/products.csv", products_list, product_fieldnames)
  
  system('clear')

def delete_product(database_list):
  products_list = database_list
  print_products(products_list)
  
  while True:
    try:
      delete_index = int(input("\nWhich product would you like to delete? Enter their ID number: "))
    except ValueError as err:
      print("\nInvalid number. Please try again!")
    else:
      break

  deleted_product = products_list.pop(delete_index)
  deletion_confirmation = input(f"Are you sure you want to delete {deleted_product}? (y or n): ")
  if deletion_confirmation == "y":
    write_csv_file("data/products.csv", products_list, product_fieldnames)
  else:
    products_list.append(deleted_product)
    write_csv_file("data/products.csv", products_list, product_fieldnames)


# COURIER MENU OPTIONS

def print_couriers(database_list):
  for courier in database_list:
    index = database_list.index(courier)
    print(f'''
    Courier ID: {index} 
    Courier name: {courier["courier_name"]} 
    Courier company: {courier["courier_company"]} 
    Courier phone: {courier["courier_phone"]}
    Courier availability: {courier["courier_availability"]}''')

def create_courier(database_list):
  couriers_list = database_list
  new_courier_name = input("\nPlease enter the courier's name: ")
  new_courier_company = input("\nPlease enter the company of the courier: ")
  new_courier_phone = input("\nPlease enter the courier's phone number: ")
  while True:
    try:
      new_courier_availability = float(input("\nPlease enter the availability of the couriers (h/week): "))
    except ValueError as err:
      print("\nInvalid number. Please try again!")
    else:
      break  
  
  new_courier = {
    "courier_name" : new_courier_name, 
    "courier_company" : new_courier_company, 
    "courier_phone" : new_courier_phone,
    "courier_availability" : new_courier_availability,
  }
  
  couriers_list.append(new_courier)

  write_csv_file("data/couriers.csv", couriers_list, courier_fieldnames)
  
def update_courier(database_list):
  couriers_list = database_list
  print_couriers(couriers_list)

  while True:
    try:
      courier_index = int(input("\nWhich courier would you like to update? Enter their ID number: "))
      chosen_courier = couriers_list[courier_index]
    except ValueError as err:
      print("\nInvalid number. Please try again!")
    else:
      break
      
  print(f'\Courier to update: {chosen_courier}')
  updated_courier_name = input("Update courier's name: ")
  updated_courier_company = input("Update courier's company: ")
  updated_courier_phone = input("Enter the courier's phone number: ")
  while True:
    try:
      updated_courier_availability = float(input("Update courier's availability: "))
    except ValueError as err:
      print("\nInvalid number. Please try again!")
    else:
      break  

  updated_courier_obj = [
    updated_courier_name, 
    updated_courier_company, 
    updated_courier_phone,
    updated_courier_availability,
  ]

  update_or_skip(courier_fieldnames, updated_courier_obj, chosen_courier)

  write_csv_file("data/couriers.csv", couriers_list, courier_fieldnames)

def delete_courier(database_list):
  couriers_list = database_list
  print_couriers(couriers_list)
  
  while True:
    try:
      delete_index = int(input("\nWhich courier would you like to delete? Enter their ID number: "))
    except ValueError as err:
      print("\nInvalid index. Please try again!")
    else:
      break

  couriers_list.pop(delete_index)
  write_csv_file("data/couriers.csv", couriers_list, courier_fieldnames)

# ORDERS MENU OPTIONS

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
  
  orders_menu()

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

  orders_menu()

def update_order(database_list):
  orders_list = database_list
  print_orders(orders_list)

  while True:
    try:
      order_index = int(input("\nWhich order status would you like to update? Enter their ID number: "))
      chosen_order = orders_list[order_index]
      print(f'\nOrder to update: {chosen_order}')
    except ValueError as err:
      print("\nInvalid number. Please try again!")
    else:
      break
  
  print(f'\Order to update: {chosen_order}\n')

  print("Please enter the new order data. (Hit 'Enter' if you don't want to change it): \n")
  
  updated_customer_name = input("\nPlease add the customer's name: ")
  updated_customer_address = input("\nPlease enter the customer's address: ")
  updated_customer_phone = input("\nPlease enter the customer's phone: ")
  print_couriers(read_csv_file("data/couriers.csv"))
  while True:
    try:
      updated_selected_courier = int(input("\nPlease select from a the available couriers above by entering their ID: "))
    except ValueError as err:
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
    updated_order_items 
    # updated_order_status
    ]

  update_or_skip(order_fieldnames, updated_customer_obj,chosen_order)

  write_csv_file("data/orders.csv", orders_list, order_fieldnames)

  orders_menu()
      
def delete_order(database_list):
  orders_list = database_list
  print_orders(orders_list)
  
  while True:
    try:
      delete_index = int(input("\nWhich order would you like to delete? Enter their ID number: "))
    except ValueError as ve:
      print("\nInvalid number. Please try again!")
    else:
      break

  deleted_order = orders_list.pop(delete_index)
  deletion_confirmation = input(f"Are you sure you want to delete {deleted_order}? (y or n): ")
  if deletion_confirmation == "y":
    write_csv_file("data/orders.csv", orders_list, order_fieldnames)
  else:
    orders_list.append(deleted_order)
    write_csv_file("data/orders.csv", orders_list, order_fieldnames)

  orders_menu()
      

# MAIN MENU
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
  database_list = read_csv_file("data/products.csv")
  # print(database_list)
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
    system('clear')
    products_menu_func = products_menu_options[chosen_menu_option]
    products_menu_func(database_list)
    if chosen_menu_option != "0":
      products_menu() 
    
  except KeyError as ke:
    print(f'{ke} is an invalid number, please try again!')
    products_menu()
    system('clear')

# COURIER MENU
def couriers_menu():
  database_list = read_csv_file("data/couriers.csv")
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
    system('clear')
    courier_menu_func = courier_menu_options[chosen_menu_option]
    courier_menu_func(database_list)
    if chosen_menu_option != "0":
      couriers_menu()
    
  except KeyError as ke:
    print(f'{ke} is an invalid number, please try again!')
    couriers_menu()
    system('clear')

# ORDERS MENU
def orders_menu():
  database_list = read_csv_file("data/orders.csv")
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
    system('clear')
    orders_menu_func = orders_menu_options[chosen_menu_option]
    orders_menu_func(database_list)
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


