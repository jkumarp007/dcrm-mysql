""" 
pip install mysql
pip install mysql-connector
pip install mysql-connector-python
 """
import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='user',
    password='user'
)

#prepair a cursor object
cursorObject = database.cursor()

# create a database

cursorObject.execute('CREATE DATABASE dcrm')

print('All Done')