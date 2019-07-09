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
        self.db_connection = sqlite3.connect(self.db_location)

    def create_db(self):
        accounts_sql = f"""CREATE TABLE {self.accounts_table_name}
            (id integer PRIMARY KEY, user_id BIGINT NOT NULL, team_id BIGINT NOT NULL, role_id BIGINT NOT NULL)"""
        if self.db_connection is not None:
            self.db_connection.execute(accounts_sql)

    def insert_row(self, row):
        row_sql = f"""INSERT INTO {self.accounts_table_name} (user_id, team_id, role_id)
            VALUES(?, ?, ?)"""
        if self.db_connection is not None:
            self.db_connection.execute(row_sql, row)
            return self.db_connection.lastrowid

    def reset_db(self):
        if not os.path.exists(os.path.dirname(__file__) + "/accounts_db.sqlite3"):
            self.create_db()

        drop_table = f"DROP TABLE {self.accounts_table_name}"
        self.db_connection.execute(drop_table)
        self.initialize()

    def get_account_by_id(self, id):
        sql = f"SELECT * FROM {self.accounts_table_name} WHERE ID = {id}"
        if self.db_connection is not None:
            self.db_connection.execute(sql)
            return self.db_connection.fetchone()

    def get_accounts_by_role_id(self, role_id):
        sql = f"SELECT * FROM {self.accounts_table_name} WHERE ID = {role_id}"
        if self.db_connection is not None:
            self.db_connection.execute(sql)
            return self.db_connection.fetchall()

if __name__ == "__main__":
    dm = DataManager()
    dm.reset_db()


