import os
import fdb
from fdb.fbcore import Error

hostDB = 'localhost'
DB = '/var/REDStore/RedStore.fdb'
userLogin = 'SYSDBA'
userPassword ='000000'

def readAppTable():
    try:
        connection = fdb.connect(host=hostDB, database=DB, user=userLogin, password=userPassword, charset='UTF8')
        cur = connection.cursor()
        print("Connected to database.")

        cur.execute('select * from APP') 
        result = cur.fetchall()
        print("Information")
        for row in result:
            print(row[1]) #title
            print(row[2]) #description
            print(row[3]) #icon
            print("id -", row[0]) #id
        
        cur.close()
    except fdb.Error as error:
        print("[Error-#101] - Module \"fdb\" operation error.") 
    finally:
        if connection:
            connection.close()
            print("Connection with database is closed.")

def addAppTable():
    try:
        connection = fdb.connect(host=hostDB, database=DB, user=userLogin, password=userPassword, charset='UTF8')
        cur = connection.cursor()
        print("Connected to database.")

        request = """INSERT INTO AUTHORS 
        (ID,FIRST_NAME, LAST_NAME, LINK) 
        VALUES (NULL, 'A','B','vom');"""
        cur.execute(request) 
        connection.commit()
        print("Mission Completed.")

        cur.close()
    except fdb.Error as error:
        print("[Error-#101] - Module \"fdb\" operation error.") 
    finally:
        if connection:
            connection.close()
            print("Connection with database is closed.")

if __name__ == "__main__":
    addAppTable()
