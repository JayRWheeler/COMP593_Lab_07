import os
import inspect
from faker import Faker
import sqlite3
import random
import datetime


def main():
    global db_path
    db_path = os.path.join(get_script_dir(), 'social_network.db')

    create_people_table()
    
    populate_people_table()


def create_people_table():
    """Creates the people table in the database"""
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute('''CREATE TABLE people (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    address TEXT NOT NULL,
                    email TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL);''')
    con.commit()
    con.close()


def populate_people_table():
    """Populates the people table with 200 fake people"""
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    fake = Faker()
    for i in range(200):
        name = fake.name()
        age = random.randint(1, 100)
        address = fake.address()
        email = fake.email()
        phone = fake.phone_number()
        created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        updated_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cur.execute("INSERT INTO people (name, age, address, email, phone, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                    (name, age, address, email, phone, created_at, updated_at))
        con.commit()
    con.close()


def get_script_dir():
    """Determines the path of the directory in which this script resides

    Returns:
        str: Full path of the directory in which this script resides
    """
    script_path = os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)
    return os.path.dirname(script_path)


if __name__ == '__main__':
   main()