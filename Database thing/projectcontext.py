# Test the SQL connector package

import mysql.connector

con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='oscar_orders')
c = con.cursor()

c.execute("""SELECT * FROM client""")
for row in c:
  print('Client ID', row[0])
  print('Name', row[1])
c.close()