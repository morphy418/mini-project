from file_handlers.file_management import deletion_confirmation, write_csv_file, update_or_skip, deletion_confirmation
from file_handlers.fieldnames import product_fieldnames
from src.db.db import delete_item_from_db, insert_new_item_into_db, update_item_in_db, delete_item_from_db
from os import system

def print_products(products_list):
  for product in products_list:
    print(f'''
    Product ID: {product["product_id"]} 
    Name: {product["product_name"]} 
    Type: {product["product_type"]} 
    Price: {product["product_price"]}''')
  
def create_new_product(products_list):

  new_product_name = input("\nPlease add a New Product: ")
  new_product_type = input("\nPlease enter the type of the new product: ")
  while True: 
    try:
      new_product_price = float(input("\nPlease enter the price of the new product: "))
    except ValueError as ve:
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
  insert_new_item_into_db("products", product_fieldnames, new_product)
  
  system('clear')
  
def update_product(products_list):
  print_products(products_list)

  while True:
    try:
      updated_product_id = int(input("\nWhich product would you like to update? Enter their ID number: "))

      for product in products_list:
        if product["product_id"] == updated_product_id:
          chosen_product = product

      print(chosen_product)
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
      if ve.args[0] == "could not convert string to float: ''":
        updated_product_price = None
        break
      print("\nInvalid number. Please try again!")
    else:
      break

  updated_product_obj = [
    updated_product_name, 
    updated_product_type, 
    updated_product_price
  ]

  updated_product = update_or_skip(product_fieldnames, updated_product_obj, chosen_product)
 
  update_item_in_db("products", product_fieldnames, updated_product, updated_product_id)
  # write_csv_file("data/products.csv", products_list, product_fieldnames)
  
  system('clear')

def delete_product(products_list):
  print_products(products_list)
  
  while True:
    try:
      deletion_id = int(input("\nWhich product would you like to delete? Enter their ID number: "))
    except ValueError as err:
      print("\nInvalid number. Please try again!")
    else:
      break

  product_deleted = deletion_confirmation(products_list, deletion_id, "product")
  delete_item_from_db("products", product_fieldnames, deletion_id, product_deleted)

  # write_csv_file("data/products.csv", products_list_deleted, product_fieldnames)
  