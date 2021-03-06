from pymysql import IntegrityError
from file_handlers.file_management import deletion_confirmation, write_csv_file, update_or_skip, deletion_confirmation
from file_handlers.fieldnames import courier_fieldnames
from src.db.db import delete_item_from_db, insert_new_item_into_db, update_item_in_db
from prettytable import PrettyTable

def print_couriers(couriers_list):
  table = PrettyTable()
  for c in courier_fieldnames:
    table.add_column(c, [])
  for dct in couriers_list:
    table.add_row([dct.get(c, "") for c in courier_fieldnames])
  print(table)

def print_chosen_courier(item, fieldnames):
  table = PrettyTable()
  table.field_names = fieldnames
  table.add_row(item.values())
  print(table)

def create_courier(couriers_list):
  print_couriers(couriers_list)
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
  
  insert_new_item_into_db("couriers", courier_fieldnames, new_courier)
  print_chosen_courier(new_courier, courier_fieldnames[1:])
  print("New courier has been created!")
  
def update_courier(couriers_list):
  print_couriers(couriers_list)

  while True:
    try:
      updated_courier_id = int(input("\nWhich courier would you like to update? Enter their ID number: "))
      for courier in couriers_list:
        if updated_courier_id not in [dict['courier_id'] for dict in couriers_list]:
          raise ValueError
        elif courier["courier_id"] == updated_courier_id:
          chosen_courier = courier
  
    except ValueError as err:
      print("\nInvalid number. Please try again!")
    else:
      break
  
  print_chosen_courier(chosen_courier, courier_fieldnames)
  print("Please enter the new courier data. (Hit 'Enter' if you don't want to change it): \n")

  updated_courier_name = input("Update courier's name: ")
  updated_courier_company = input("Update courier's company: ")
  updated_courier_phone = input("Enter the courier's phone number: ")
  while True:
    try:
      updated_courier_availability = float(input("Update courier's availability: "))
    except ValueError as ve:
      if ve.args[0] == "could not convert string to float: ''":
        updated_courier_availability = None
        break
      print("\nInvalid number. Please try again!")
    else:
      break  

  updated_courier = [
    updated_courier_name, 
    updated_courier_company, 
    updated_courier_phone,
    updated_courier_availability,
  ]

  updated_courier = update_or_skip(courier_fieldnames, updated_courier, chosen_courier)
  update_item_in_db("couriers", courier_fieldnames, updated_courier, updated_courier_id)
  print_chosen_courier(updated_courier, courier_fieldnames)
  print("Courier has been updated!")

def delete_courier(couriers_list):
  print_couriers(couriers_list)
  
  while True:
    try:
      deletion_id = int(input("\nWhich courier would you like to delete? Enter their ID number: "))
      if deletion_id not in [dict['courier_id'] for dict in couriers_list]:
          raise ValueError
      courier_deleted = deletion_confirmation(couriers_list, deletion_id, "courier")
      delete_item_from_db("couriers", courier_fieldnames, deletion_id, courier_deleted)
    except ValueError as va:
      print("\nInvalid index. Please try again!")
    except IntegrityError as ie:
      print("\nThis item is assigned to another table and cannot be deleted. Please choose another one.")
    else:
      break
  
  print_chosen_courier(courier_deleted, courier_fieldnames)
  print(f"Courier has been successfully deleted from database.")
