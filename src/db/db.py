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

  cursor.execute(f'SELECT {selection} FROM {table}')
  rows = cursor.fetchall()

  

  data = []
  # for row in rows:
  #   new_data = {
  #     fieldnames[0] : row[0], 
  #     fieldnames[1] : row[1], 
  #     fieldnames[2] : row[2]
  #     }
      
  for row in rows:
    # print(row)
    new_item = {}
    for index in range(len(fieldnames)):

      new_item[fieldnames[index]] = row[index]
  
    data.append(new_item)

  cursor.close()
  connection.close()
  # print(data)
  return data


  

# read_products_db("products", product_fieldnames)