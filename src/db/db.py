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

  set_string = ""

  for key, value in item.items():
    set_string += f"{key} = '{value}',"
  
  print(set_string[:-1])

  sql = f"UPDATE {table} set {set_string[:-1]} where {fieldnames[0]} = {item_id} "
    
  cursor.execute(sql)

  connection.commit()
  cursor.close()
  connection.close()

def delete_item_from_db(table, fieldnames, item_id, item_deleted):


  connection = pymysql.connect(host=host,
                              user=user,
                              password=password,
                              database=database,
                              )

  cursor = connection.cursor()

  sql = f"DELETE FROM {table} WHERE {fieldnames[0]} = {item_id}"

  print(f"{item_deleted} has been successfully deleted from database.")
  cursor.execute(sql)

  connection.commit()
  cursor.close()
  connection.close()

def read_list_from_orders_table(fieldnames):
  connection = pymysql.connect(host=host,
                              user=user,
                              password=password,
                              database=database,)
  cursor = connection.cursor()
  
  # selection = ','.join(fieldnames)

  cursor.execute(f'''
  SELECT orders.order_id, orders.customer_name, orders.customer_address, orders.customer_phone, orders.selected_courier, orders.order_status, products.product_name
  FROM orders
  JOIN products_on_orders ON orders.order_id = products_on_orders.order_id
  JOIN products ON products_on_orders.product_id = products.product_id''')
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

def insert_new_order_into_db(fieldnames, item):

  connection = pymysql.connect(host=host,
                              user=user,
                              password=password,
                              database=database,
                              )

  cursor = connection.cursor()

  no_id_fieldnames = fieldnames[1:-1]
  print(no_id_fieldnames)
  selection = ','.join(no_id_fieldnames)
  number_of_fieldnames = len(no_id_fieldnames)

  val1 = ()
  for index in range(number_of_fieldnames):
    val1 += (item[no_id_fieldnames[index]],)

  sql1 = f"INSERT INTO orders ({selection}) VALUES ({(number_of_fieldnames-1)*'%s,'}%s);"
    
  cursor.execute(sql1, val1)
  connection.commit()
  order_id = cursor.lastrowid
  cursor.close()

  val2 = []
  for item in item["order_items"]:
    val2.append((order_id, item))

  cursor = connection.cursor()
  sql2 = f"INSERT INTO products_on_orders (order_id, product_id) values (%s, %s)"
  
  cursor.executemany(sql2, val2)
  connection.commit()
  cursor.close()
  
  connection.close()