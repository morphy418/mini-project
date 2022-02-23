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
  JOIN products ON products_on_orders.product_id = products.product_id
  ORDER BY order_id''')
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

def update_order_in_db(fieldnames, order, order_id):
  connection = pymysql.connect(host=host,
                              user=user,
                              password=password,
                              database=database,
                              )

  cursor = connection.cursor()

  set_string = ""

  for key, value in order.items():
    if key != "order_items":
      set_string += f"{key} = '{value}',"

  sql = f"UPDATE orders set {set_string[:-1]} where {fieldnames[0]} = {order_id} "
  cursor.execute(sql)
  connection.commit()
  cursor.close()

  cursor = connection.cursor()
  sql2 = f"DELETE FROM products_on_orders WHERE order_id = {order_id}";
  cursor.execute(sql2)
  connection.commit()
  cursor.close()

  cursor = connection.cursor()
  val3 = []
  for item in order["order_items"]:
    val3.append((order_id, item))

  cursor = connection.cursor()
  sql3 = f"INSERT INTO products_on_orders (order_id, product_id) values (%s, %s)"
  
  cursor.executemany(sql3, val3)
  connection.commit()
  cursor.close()
  connection.close()

def delete_order_from_db(order_id):
  connection = pymysql.connect(host=host,
                              user=user,
                              password=password,
                              database=database,
                              )

  cursor = connection.cursor()
  sql = f"DELETE FROM products_on_orders WHERE order_id = {order_id}";
  cursor.execute(sql)
  connection.commit()
  cursor.close()

  cursor = connection.cursor()
  sql2 = f"DELETE FROM orders WHERE order_id = {order_id}";
  cursor.execute(sql2)
  connection.commit()
  cursor.close()


  connection.close()

def update_order_status_in_db(new_status, order_id):
  connection = pymysql.connect(host=host,
                                user=user,
                                password=password,
                                database=database,
                                )

  cursor = connection.cursor()
  sql = f"UPDATE orders set order_status = '{new_status}' where order_id = {order_id} "
  cursor.execute(sql)
  connection.commit()
  cursor.close()