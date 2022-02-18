from file_handlers.file_management import deletion_confirmation, write_csv_file, update_or_skip, deletion_confirmation
from file_handlers.fieldnames import courier_fieldnames
from src.db.db import delete_item_from_db, insert_new_item_into_db, update_item_in_db

def print_couriers(couriers_list):
  for courier in couriers_list:
    print(f'''
    Courier ID: {courier["courier_id"]} 
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
      updated_courier_id = int(input("\nWhich courier would you like to update? Enter their ID number: "))
      for courier in couriers_list:
        if courier["courier_id"] == updated_courier_id:
          chosen_courier = courier
    except ValueError as err:
      print("\nInvalid number. Please try again!")
    else:
      break
      
  print(f'\nCourier to update: {chosen_courier}')
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

  updated_courier = update_or_skip(courier_fieldnames, updated_courier_obj, chosen_courier)
  update_item_in_db("couriers", courier_fieldnames, updated_courier, updated_courier_id)

  # write_csv_file("data/couriers.csv", couriers_list, courier_fieldnames)

def delete_courier(couriers_list):
  print_couriers(couriers_list)
  
  while True:
    try:
      deletion_id = int(input("\nWhich courier would you like to delete? Enter their ID number: "))
    except ValueError as err:
      print("\nInvalid index. Please try again!")
    else:
      break

  courier_deleted = deletion_confirmation(couriers_list, deletion_id, "courier")
  delete_item_from_db("couriers", courier_fieldnames, deletion_id, courier_deleted)

  write_csv_file("data/couriers.csv", couriers_list, courier_fieldnames)
