from select import select
from threading import local
import pymysql
import os
from dotenv import load_dotenv

product_fieldnames = [
      "product_name", 
      "product_type", 
      "product_price", 
      ]

def read_products_db(table, fieldnames):
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
  # print(selection)

  cursor.execute(f'SELECT product_name,product_type,product_price FROM {table}')
  rows = cursor.fetchall()

  data = []
  for row in rows:
    new_data = {
      'product_name' : row[0], 
      'product_type' : row[1], 
      'product_price': row[2]
      }

    data.append(new_data)

  cursor.close()
  connection.close()
  return data


  

# read_products_db("products", product_fieldnames)