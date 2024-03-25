import json
import pymysql
import os

class kardb:
    def __init__(self, dbname, host="localhost", user="root", passwd=""):
        self.dbname = dbname
        self.docname = 'main'
        self.host = host
        self.user = user

    def create_database(self):
        query = f'create database if not exists {self.dbname}'
        mycursor.execute(query)
        mycursor.commit()

    def connect(self):
        db = pymysql.connect(
            host = self.host,
            user = user,
            passwd = passwd,
            database = self.dbname
            )
        mycursor = db.cursor()

    def disconnect(self):
        mycursor.close()
        db.close()