import csv

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
    writer.writerows(list)

def update_or_skip(fieldnames, update_object, chosen_item):
  for update in update_object:
    if update != "" and update != None:
      index = update_object.index(update)
      chosen_item[fieldnames[index]] = update_object[index]

def deletion_confirmation(list, deletion_index):
  item_to_delete = list[deletion_index]
  deletion_confirmation = input(f"Are you sure you want to delete {item_to_delete}? (y or n): ")
  if deletion_confirmation == "y":
    list.pop(deletion_index)

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