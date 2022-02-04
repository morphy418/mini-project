from os import system
import csv

# FILE MANAGEMENT

def read_file(file_name):
  with open(file_name, "r") as open_file:
    file_contents = open_file.readlines()
    return file_contents

def write_file(file_name, list):
  with open(file_name, "w") as database_file:
    for item in list:
      database_file.write(item.strip() + '\n')

def generate_list_from_database(database):
  with open(database, 'r') as data_file:
    data = data_file.readlines()
    data_list = [item.strip() for item in data]
  return data_list

def read_csv_file(file_name):
  with open(file_name, "r") as database_file:
    reader = csv.DictReader(database_file)
    data = []
    for item in reader:
      data.append(item)
    return data

def write_csv_file(file_name, list):
  with open(file_name, "w") as database_file:
    fieldnames = [
      "customer_name", 
      "customer_address", 
      "customer_phone", 
      "selected_courier", 
      "order_status"]

    writer = csv.DictWriter(database_file, fieldnames=fieldnames)

    writer.writeheader()

    for dict_item in list:
      print(dict_item)
      writer.writerow(dict_item)

#MAIN MENU OPTIONS
def exit_app():
  print("\nYou exited the app.")

# PRODUCT MENU OPTIONS

def print_products(database_list):
  products_list = database_list

  for product in products_list:
    index = products_list.index(product)
    print(f'{index} - {product.strip()}')
  
def create_new_product(database_list):
  products_list = database_list

  new_product_name = input("\nPlease add a New Product: ")
  new_product_type = input("\nPlease enter the type of the new product: ")
  new_product_price = float(input("\nPlease enter the price of the new product: "))
  new_product = f"name : {new_product_name}, type : {new_product_type}, price : {new_product_price}"
  
  products_list.append(new_product)

  write_file("data/products.txt", products_list)
  
  system('clear')
  
def update_product(database_list):
  products_list = database_list
  print_products(products_list)

  while True:
    try:
      update_index = int(input("\nWhich product would you like to update? Enter their index number: "))
      print(f'\nItem to update: {products_list[update_index]}')
    except ValueError as err:
      print("\nInvalid index. Please try again!")
    else:
      updated_product_name = input("Updated Product Name: ")
      updated_product_type = input("Updated Product Type: ")
      updated_product_price = float(input("Updated Product Price: "))
      
      updated_product = f"name : {updated_product_name}, type : {updated_product_type}, price : {updated_product_price}"

      products_list[update_index] = updated_product

      write_file("data/products.txt", products_list)
      
      system('clear')

      break

def delete_product(database_list):
  products_list = database_list
  print_products(products_list)
  
  while True:
    try:
      delete_index = int(input("\nWhich product would you like to delete? Enter their index number: "))
    except ValueError as err:
      print("\nInvalid index. Please try again!")

    else:
      products_list.pop(delete_index)

      write_file("data/products.txt", products_list)
      
      break

# COURIER MENU OPTIONS

def print_couriers(database_list):
  for product in database_list:
    index = database_list.index(product)
    print(f'{index} - {product.strip()}')

def create_courier(database_list):
  couriers_list = database_list
  new_courier_name = input("\nPlease add a new courier name: ")
  new_courier_company = input("\nPlease enter the company of the courier: ")
  new_courier_availability = float(input("\nPlease enter the availability of the couriers (h/week): "))
  new_courier = f"name : {new_courier_name}, company : {new_courier_company}, availability : {new_courier_availability}hour/week"
  
  couriers_list.append(new_courier)

  write_file("data/couriers.txt", couriers_list)
  
def update_courier(database_list):
  couriers_list = database_list
  print_products(couriers_list)

  while True:
    try:
      update_index = int(input("\nWhich courier would you like to update? Enter their index number: "))
      print(f'\nItem to update: {couriers_list[update_index]}')
    except ValueError as err:
      print("\nInvalid index. Please try again!")
    else:
      updated_courier_name = input("Update courier's name: ")
      updated_courier_company = input("Update courier's company: ")
      updated_courier_availability = float(input("Update courier's availability: "))
      
      updated_product = f"name : {updated_courier_name}, type : {updated_courier_company}, price : {updated_courier_availability}"

      couriers_list[update_index] = updated_product

      write_file("data/products.txt", couriers_list)
  
      break

def delete_courier(database_list):
  couriers_list = database_list
  print_products(couriers_list)
  
  while True:
    try:
      delete_index = int(input("\nWhich courier would you like to delete? Enter their index number: "))
    except ValueError as err:
      print("\nInvalid index. Please try again!")

    else:
      couriers_list.pop(delete_index)

      write_file("data/couriers.txt", couriers_list)
      
      break

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
    Order status: {order["order_status"]}''')

def create_order(database_list):
  orders_list = database_list

  customer_name = input("\nPlease add the customer's name: ")
  customer_address = input("\nPlease enter the customer's address: ")
  customer_phone = input("\nPlease enter the customer's phone: ")
  print_couriers(generate_list_from_database("data/couriers.txt"))
  selected_courier = int(input("Please select from a the available couriers above by entering their ID: "))
  order_status = "preparing"

  new_order = f'''
  New Order:
  Customer: {customer_name} 
  Customer's address: {customer_address} 
  Customer's phone: {customer_phone}
  Courier: {selected_courier}
  Order status: {order_status}'''
  print(new_order)
  
  new_order_dict = {
    "customer_name": customer_name,
    "customer_address" : customer_address,
    "customer_phone" : customer_phone,
    "selected_courier" : selected_courier,
    "order_status" : order_status
    }

  print(new_order_dict)

  orders_list.append(new_order_dict)

  write_csv_file("data/orders.csv", orders_list)
  
  orders_menu()

def update_order_status(database_list):
  orders_list = database_list
  print_orders(orders_list)

  while True:
    try:
      order_index = int(input("\nWhich order status would you like to update? Enter their ID number: "))
      print(f'\nOrder status to update: {orders_list[order_index]}')
    except ValueError as err:
      print("\nInvalid index. Please try again!")
    else:
    
      while True:
        try:
          order_status_list = ["preparing", "on the way", "delivered", "cancelled"]
          for status in order_status_list:
            print(f'{order_status_list.index(status)} - {status}')
          status_index= int(input('\n Please choose an order status (enter their number)'))
        except ValueError as err:
          print("\nInvalid index. Please try again!")
        else:
          print(orders_list[order_index]["order_status"])
          print(order_status_list[status_index])

          orders_list[order_index]["order_status"] = order_status_list[status_index]
          write_csv_file("data/orders.csv", orders_list)

          orders_menu()
          break

def update_order(database_list):
  orders_list = database_list
  print_orders(orders_list)

  while True:
    try:
      order_index = int(input("\nWhich order status would you like to update? Enter their ID number: "))
      chosen_order = orders_list[order_index]
      print(f'\nOrder to update: {chosen_order}')
    except ValueError as err:
      print("\nInvalid index. Please try again!")
    else:
      
      print("Please enter the new order data. (Hit 'Enter' if you don't want to change it): \n")
      
      updated_customer_name = input("\nPlease add the customer's name: ")
      updated_customer_address = input("\nPlease enter the customer's address: ")
      updated_customer_phone = input("\nPlease enter the customer's phone: ")
      print_couriers(generate_list_from_database("data/couriers.txt"))
      updated_selected_courier = int(input("\nPlease select from a the available couriers above by entering their ID: "))

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
        # updated_order_status
        ]

      fieldnames = [
      "customer_name", 
      "customer_address", 
      "customer_phone", 
      "selected_courier", 
      # "order_status"
      ]

      for update in updated_customer_obj:
        # print(f'user input: {update}\n')
        if update != "" and update != None:
          index = updated_customer_obj.index(update)
          chosen_order[fieldnames[index]] = updated_customer_obj[index]

      write_csv_file("data/orders.csv", orders_list)

      orders_menu()
      break

def delete_order(database_list):
  orders_list = database_list
  print_orders(orders_list)
  
  while True:
    try:
      delete_index = int(input("\nWhich order would you like to delete? Enter their index number: "))
    except ValueError as err:
      print("\nInvalid index. Please try again!")

    else:
      orders_list.pop(delete_index)

      write_csv_file("data/orders.csv", orders_list)
      orders_menu()
      break

# MAIN MENU
def main_menu(*args):
  system('clear')
  print("\nWelcome to Git Cat Cafe!")

  user_input = input("""
  Main Menu Options:

  (1-Product Menu) 
  (2-Courier Menu)
  (3-Order Menu)
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
  database_list = generate_list_from_database("data/products.txt")

  chosen_menu_option = input("""
  Products Menu Options:

  (1-Print Products) 
  (2-Create New Product) 
  (3-Update Existing Product) 
  (4-Delete Product) 
  (0-Return to Main Menu)

  Please enter the corresponding number: """)

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
  database_list = generate_list_from_database("data/couriers.txt")

  chosen_menu_option = input("""
  Products Menu Options:

  (1-Print Couriers) 
  (2-Create New Couriers) 
  (3-Update Existing Courier) 
  (4-Delete Courier) 
  (0-Return to Main Menu)

  Please enter the corresponding number: """)

  try:
    system('clear')
    courier_menu_func = courier_menu_options[chosen_menu_option]
    courier_menu_func(database_list)
    couriers_menu()
    
  except KeyError as ke:
    print(f'{ke} is an invalid number, please try again!')
    couriers_menu()

# ORDERS MENU
def orders_menu():
  database_list = read_csv_file("data/orders.csv")

  chosen_menu_option = input("""
  Orders Menu Options:

  (1-Print Orders) 
  (2-Create New Order) 
  (3-Update Existing Order Status) 
  (4-Update Existing Order)
  (5-Delete Product) 
  (0-Return to Main Menu)

  Please enter the corresponding number: """)

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


