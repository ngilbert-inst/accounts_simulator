import os
import sqlite3


class DataManager:
    def __init__(self):
        self.accounts_table_name = "accounts"
        self.db_location = os.path.join(os.path.dirname(__file__), 'accounts_db.sqlite3')
        self.db_connection = None

    def connect(self):
        self.db_connection = sqlite3.connect(self.db_location)

    def create_db(self):
        accounts_sql = f"CREATE TABLE {self.accounts_table_name} (id integer PRIMARY KEY, user_id BIGINT, role_id BIGINT)"
        if self.db_connection is not None:
            self.db_connection.execute(accounts_sql)

    def reset_db(self):
        drop_table = f"DROP TABLE {self.accounts_table_name}"
        if self.db_connection is not None:
            self.db_connection.execute(drop_table)

if __name__ == "__main__":
    dm = DataManager()
    dm.create_db()
