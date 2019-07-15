import os
import sqlite3


class DataManager:
    def __init__(self):
        self.accounts_table_name = "accounts"
        self.db_location = os.path.join(os.path.dirname(__file__), 'accounts_db.sqlite3')
        self.db_connection = None

    def initialize(self):
        self.connect()
        self.create_db()

    def connect(self):
        self.db_connection = sqlite3.connect(self.db_location, check_same_thread=False)
        self.db_connection.row_factory = sqlite3.Row

    def create_db(self):
        accounts_sql = f"""CREATE TABLE {self.accounts_table_name}
            (id integer PRIMARY KEY, user_id integer NOT NULL, team_id integer NOT NULL, role_id integer NOT NULL, role_title TEXT)"""
        if self.db_connection is not None:
            self.db_connection.execute(accounts_sql)

    def insert_row(self, row):
        row_sql = f"""INSERT INTO {self.accounts_table_name} (user_id, team_id, role_id, role_title)
            VALUES(?, ?, ?, ?)"""

        if self.db_connection is not None:
            cur = self.db_connection.cursor()
            cur.execute(row_sql, row)
            self.db_connection.commit()
            return cur.lastrowid

    def reset_db(self):
        self.db_connection = None
        if os.path.exists(self.db_location):
            os.remove(self.db_location)
        self.create_db()
        self.connect()
        self.initialize()

    def get_account_by_id(self, id):
        sql = f"SELECT * FROM {self.accounts_table_name} WHERE id = {id}"
        return self.__get_row(sql)

    def get_account_by_user_id(self, user_id):
        sql = f"SELECT * FROM {self.accounts_table_name} WHERE user_id = {user_id}"
        return self.__get_row(sql)

    def get_accounts_by_role_id(self, role_id):
        sql = f"SELECT * FROM {self.accounts_table_name} WHERE role_id = {role_id}"
        return self.__get_rows(sql)

    def get_accounts_by_team_id(self, team_id):
        sql = f"SELECT * FROM {self.accounts_table_name} WHERE team_id = {team_id}"
        return self.__get_rows(sql)

    def __get_row(self, sql):
        cur = self.db_connection.cursor()
        cur.execute(sql)
        row = cur.fetchone()
        if row is None:
            row = [ dict() ]
        else:
            row = [ dict(row) ]
        return row

    def __get_rows(self, sql):
        cur = self.db_connection.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        if rows is None:
            rows = list()
        else:
            rows = [ dict(x) for x in rows ]
        return rows

if __name__ == "__main__":
    dm = DataManager()
    dm.reset_db()
    dm.insert_row((1, 1, 1, "Team Lead"))
    dm.insert_row((2, 2, 1, "Team Lead"))
    dm.insert_row((3, 2, 2, "Software Engineer"))
    dm.insert_row((4, 2, 2, "Software Engineer"))
    dm.insert_row((10, 2, 2, "Software Engineer"))
    dm.insert_row((20, 1, 2, "Software Engineer"))
