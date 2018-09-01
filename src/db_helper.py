import sqlite3
import os


class DbHelper():
    db_file = 'db/database.sqlite'

    payments_discounts_table = "payments_discounts"

    def __init__(self):
        if not os.path.exists('db'):
            os.makedirs('db')

        self.conn = sqlite3.connect(self.db_file)
        self.db = self.conn.cursor()
        self.init_db()

    @staticmethod
    def get_payments_discounts_columns():
        return [["payment_id_", "TEXT"],
                ["payment_description", "TEXT"],
                ["payment_amount_currency", "TEXT"],
                ["payment_amount_value", "TEXT"],
                ["discount_applied_value", "TEXT"]]

    def init_db(self):
        query = "CREATE TABLE IF NOT EXISTS payments_discounts ("

        columns = self.get_payments_discounts_columns()
        for idx, entry in enumerate(columns):
            query += entry[0] + " " + entry[1]
            if idx != len(columns) - 1:
                query += ", "

        query += ")"

        print("Executing " + query)

        self.db.execute(query)
        self.conn.commit()

    def add_payment_to_database(self, payment_id_,
                                payment_description,
                                payment_amount_currency,
                                payment_amount_value,
                                discount_applied_value):
        query = "INSERT INTO " + self.payments_discounts_table + " ( "
        columns = self.get_payments_discounts_columns()
        for idx, entry in enumerate(columns):
            query += entry[0]
            if idx != len(columns) - 1:
                query += ", "

        query += ") VALUES (" \
                 "'{payment_id_}' , " \
                 "'{payment_description}' , " \
                 "'{payment_amount_currency}' , " \
                 "'{payment_amount_value}' , " \
                 "'{discount_applied_value}');".format(payment_id_=payment_id_,
                                                       payment_description=payment_description,
                                                       payment_amount_currency=payment_amount_currency,
                                                       payment_amount_value=payment_amount_value,
                                                       discount_applied_value=discount_applied_value)
        print("Executing " + query)

        self.db.execute(query)
        self.conn.commit()

    def get_payments_from_database(self, limit=10):
        set_limit = True
        if limit is None:
            set_limit = False

        query = "SELECT "
        columns = self.get_payments_discounts_columns()
        for idx, entry in enumerate(columns):
            query += entry[0]
            if idx != len(columns) - 1:
                query += ", "
        query += " FROM " + self.payments_discounts_table
        if set_limit:
            query += " LIMIT " + str(limit)

        print(query)
        self.db.execute(query)
        return self.db.fetchall()


if __name__ == "__main__":
    db_helper = DbHelper()

    db_helper.add_payment_to_database("1", "test", "eur", "20", "")
    print(db_helper.get_payments_from_database(2))
