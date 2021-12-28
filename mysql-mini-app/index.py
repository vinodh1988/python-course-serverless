import mysql.connector

my_connection=mysql.connector.connect(
        host ="13.233.83.152",
        user="peter",
        passwd="Pass@123"
  )

print(my_connection)