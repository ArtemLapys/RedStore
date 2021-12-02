import sqlite3

def readAppTable():
    connectToDB = sqlite3.connect('/var/REDStore/RedStore.fdb')