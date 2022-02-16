from select import select
from threading import local
import pymysql
import os
from dotenv import load_dotenv

product_fieldnames = [
      "product_id",
      "product_name", 
      "product_type", 
      "product_price", 
      ]

def read_list_from_db(table, fieldnames):
  load_dotenv()
  host = os.environ.get("mysql_host")
  user = os.environ.get("mysql_user")
  password = os.environ.get("mysql_pass")
  database = os.environ.get("mysql_db")

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
    for index in range(len(fieldnames)):
      new_item[fieldnames[index]] = row[index]
    data.append(new_item)

  cursor.close()
  connection.close()
  return data

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

def insert_new_item_into_db(table, fieldnames, item):

  load_dotenv()
  host = os.environ.get("mysql_host")
  user = os.environ.get("mysql_user")
  password = os.environ.get("mysql_pass")
  database = os.environ.get("mysql_db")

  # Establish a database connection
  connection = pymysql.connect(host=host,
                              user=user,
                              password=password,
                              database=database,
                              )

  # A cursor is an object that represents a DB cursor, which is used to manage the context of a fetch operation.
  cursor = connection.cursor()

  fieldnames.pop(0)
  selection = ','.join(fieldnames)
  number_of_fieldnames = len(fieldnames)

  val = ()
  for index in range(number_of_fieldnames):
    val += (item[fieldnames[index]],)

  sql = f"INSERT INTO {table}({selection}) VALUES ({(number_of_fieldnames-1)*'%s,'}%s)"
    
  cursor.execute(sql, val)

  # Add code here to insert a new record

  connection.commit()
  cursor.close()
  connection.close()
