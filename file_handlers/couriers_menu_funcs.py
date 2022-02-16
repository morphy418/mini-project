from file_handlers.file_management import deletion_confirmation, write_csv_file, update_or_skip, deletion_confirmation
from file_handlers.fieldnames import courier_fieldnames
from src.db.db import insert_new_item_into_db

def print_couriers(couriers_list):
  for courier in couriers_list:
    print(f'''
    Courier ID: {courier[courier_id]} 
    Courier name: {courier["courier_name"]} 
    Courier company: {courier["courier_company"]} 
    Courier phone: {courier["courier_phone"]}
    Courier availability: {courier["courier_availability"]}''')

def create_courier(couriers_list):
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
  insert_new_item_into_db("couriers", courier_fieldnames, new_courier)
  
def update_courier(couriers_list):
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
    except ValueError as ve:
      if ve.args[0] == "could not convert string to float: ''":
        updated_courier_availability = None
        break
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

def delete_courier(couriers_list):
  print_couriers(couriers_list)
  
  while True:
    try:
      deletion_index = int(input("\nWhich courier would you like to delete? Enter their ID number: "))
    except ValueError as err:
      print("\nInvalid index. Please try again!")
    else:
      break

  deletion_confirmation(couriers_list, deletion_index)

  write_csv_file("data/couriers.csv", couriers_list, courier_fieldnames)
