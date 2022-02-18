from select import select
from threading import local
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# product_fieldnames = [
#       "product_id",
#       "product_name", 
#       "product_type", 
#       "product_price", 
#       ]

# products_list = [
#   {'product_name': 'espresso', 'product_type': 'hot bev', 'product_price': 2.2}, 
#   {'product_name': 'latte', 'product_type': 'hot bev', 'product_price': 2.2}, 
#   {'product_name': 'espresso', 'product_type': 'hot bev', 'product_price': 2.2}, 
#   {'product_name': 'cappuccino', 'product_type': 'hot bev', 'product_price': 2.2}, 
#   {'product_name': 'orange juice', 'product_type': 'juice', 'product_price': 2.2}, 
#   {'product_name': 'grapefruit juice', 'product_type': 'juice', 'product_price': 2.2}, 
#   {'product_name': 'croissant', 'product_type': 'hot bev', 'product_price': 2.2}, 
#   {'product_name': 'ain au chocolat', 'product_type': 'pastry', 'product_price': 2.2}, 
#   {'product_name': 'earl grey', 'product_type': 'hot bev', 'product_price': 2.2}]

# item = {'product_name': 'espresso', 'product_type': 'hot bev', 'product_price': 2.2}

def read_list_from_db(table, fieldnames):

  connection = pymysql.connect(host=host,
                              user=user,
                              password=password,
                              database=database,)
  cursor = connection.cursor()
  
  selection = ','.join(fieldnames)

  cursor.execute(f'SELECT {selection} FROM {table}')
  rows = cursor.fetchall()

  data = []

  for row in rows:
    new_item = {}
    for index, fieldname in enumerate(fieldnames):
      new_item[fieldname] = row[index]
    data.append(new_item)

  cursor.close()
  connection.close()
  return data


def insert_new_item_into_db(table, fieldnames, item):

  connection = pymysql.connect(host=host,
                              user=user,
                              password=password,
                              database=database,
                              )

  cursor = connection.cursor()

  no_id_fieldnames = fieldnames[:]
  no_id_fieldnames.pop(0)
  selection = ','.join(no_id_fieldnames)
  number_of_fieldnames = len(no_id_fieldnames)

  val = ()
  for index in range(number_of_fieldnames):
    val += (item[no_id_fieldnames[index]],)

  sql = f"INSERT INTO {table}({selection}) VALUES ({(number_of_fieldnames-1)*'%s,'}%s)"
    
  cursor.execute(sql, val)

  connection.commit()
  cursor.close()
  connection.close()

def update_item_in_db(table, fieldnames, item, item_id):

  connection = pymysql.connect(host=host,
                              user=user,
                              password=password,
                              database=database,
                              )

  cursor = connection.cursor()

  # no_id_fieldnames = fieldnames[:]
  # no_id_fieldnames.pop(0)
  # selection = ','.join(fieldnames)
  number_of_fieldnames = len(fieldnames)

  # for index in range(number_of_fieldnames-1):
  #   set_string += f"{fieldnames[index+1]} = {item[fieldnames[index+1]]},"
  set_string = ""

  for key, value in item.items():
    set_string += f"{key} = '{value}', "
  
  print(set_string[:-2])

  sql = f"UPDATE {table} set {set_string[:-2]} where {fieldnames[0]} = {item_id} "
    
  cursor.execute(sql)

  connection.commit()
  cursor.close()
  connection.close()
