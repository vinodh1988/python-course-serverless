import mysql.connector
import os


my_connection=mysql.connector.connect(
        host = os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        passwd=os.getenv("MYSQL_PASS")
  )

print(my_connection)