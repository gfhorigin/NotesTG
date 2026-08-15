import sqlite3

from app.config import DATABASE_NAME


class DataBase:
    def __init__(self):
        self.con = sqlite3.connect(DATABASE_NAME)
        self.cur = self.con.cursor()

    def create_database(self):
        pass

