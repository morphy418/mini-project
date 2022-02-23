from math import prod
from multiprocessing.sharedctypes import Value

from pymysql import IntegrityError
from file_handlers.file_management import deletion_confirmation, update_or_skip, deletion_confirmation
from file_handlers.fieldnames import product_fieldnames
from src.db.db import delete_item_from_db, insert_new_item_into_db, update_item_in_db, delete_item_from_db
from os import system
from prettytable import PrettyTable

def print_products(products_list):
  table = PrettyTable()
  for c in product_fieldnames:
    table.add_column(c, [])
  for dct in products_list:
    table.add_row([dct.get(c, "") for c in product_fieldnames])
  print(table)

def print_chosen_product(item, fieldnames):
  table = PrettyTable()
  table.field_names = fieldnames
  table.add_row(item.values())
  print(table)
  
def create_new_product(products_list):
  print_products(products_list)
  new_product_name = input("\nPlease add a new product name: ")
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
  
  insert_new_item_into_db("products", product_fieldnames, new_product)
  
  print_chosen_product(new_product, product_fieldnames[1:])
  print("New product has been created!")
    
def update_product(products_list):
  print_products(products_list)

  while True:
    try:
      updated_product_id = int(input("\nWhich product would you like to update? Enter their ID number: "))
      for product in products_list:
        if product["product_id"] == updated_product_id:
          chosen_product = product
        else:
          raise ValueError
    except ValueError as err:
      print("\nInvalid number. Please try again!")
    else:
      system('clear')
      break

  print_chosen_product(chosen_product, product_fieldnames)
  print("Please enter the new product data. (Hit 'Enter' if you don't want to change it): \n")

  updated_product_name = input("Updated product name: ")
  updated_product_type = input("Updated product type: ")
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

  updated_product = [
    updated_product_name, 
    updated_product_type, 
    updated_product_price
  ]

  updated_product = update_or_skip(product_fieldnames, updated_product, chosen_product)
  update_item_in_db("products", product_fieldnames, updated_product, updated_product_id)
  print_chosen_product(updated_product, product_fieldnames)
  print("Product has been updated!")

def delete_product(products_list):
  print_products(products_list)
  
  while True:
    try:
      deletion_id = int(input("\nWhich product would you like to delete? Enter their ID number: "))
      product_deleted = deletion_confirmation(products_list, deletion_id, "product")
      delete_item_from_db("products", product_fieldnames, deletion_id, product_deleted)  
    except ValueError as va:
      print("\nInvalid number. Please try again!")
    except IntegrityError as ie:
      print("\nThis item is assigned to another table and cannot be deleted. Please choose another one.")
    else:
      break
  print_chosen_product(product_deleted, product_fieldnames)
  print("The product has been successfully deleted from database.")
      