"""
Description:
Prints the name and age of all people in the Social Network database
who are age 50 or older, and saves the information to a CSV file.

Usage:
python old_people.py
"""
import os
import csv
import inspect
import sqlite3
from datetime import datetime


def main():
    script_dir = get_script_dir()
    db_path = os.path.join(script_dir, 'social_network.db')

    # Get the names and ages of all old people
    old_people_list = get_old_people(db_path)

    # Print the names and ages of all old people
    print_name_and_age(old_people_list)

    # Save the names and ages of all old people to a CSV file
    old_people_csv = os.path.join(script_dir, 'old_people.csv')
    save_name_and_age_to_csv(old_people_list, old_people_csv)


def get_old_people(db_path):
    """Queries the Social Network database for all people who are at least 50 years old.

    Returns:
        list: (name, age) of old people
    """
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    # Get the current date and time
    now = datetime.now()

    # Define an SQL query that selects the names and ages of all people who are 50 or older
    sql = '''
        SELECT name, age FROM people
        WHERE age >= 50
    '''

    # Execute the SQL query and get the results
    cur.execute(sql)
    rows = cur.fetchall()

    # Close the database connection
    con.close()

    # Convert the rows to a list of (name, age) tuples
    old_people_list = [(name, age) for (name, age) in rows]

    # Add the current date and time to each tuple in the list
    old_people_list = [(name, age, now) for (name, age) in old_people_list]

    return old_people_list


def print_name_and_age(name_and_age_list):
    """Prints name and age of all people in provided list

    Args:
        name_and_age_list (list): (name, age) of people
    """
    for (name, age, date) in name_and_age_list:
        print(f'{name} is {age} years old.')


def save_name_and_age_to_csv(name_and_age_list, csv_path):
    """Saves name and age of all people in provided list

    Args:
        name_and_age_list (list): (name, age) of people
        csv_path (str): Path of CSV file
    """
    # Define the header row for the CSV file
    header = ['Name', 'Age', 'Date']

    # Open the CSV file for writing
    with open(csv_path, 'w', newline='') as csvfile:
        # Create a CSV writer object
        writer = csv.writer(csvfile)

        # Write the header row to the CSV file
        writer.writerow(header)

        # Write the data rows to the CSV file
        for (name, age, date) in name_and_age_list:
            writer.writerow([name, age, date])


def get_script_dir():
    """Determines the path of the directory in which this script resides

    Returns:
        str: Full path of the directory in which this script resides
    """
    script_path = os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)
    return os.path.dirname(script_path)


if __name__ == '__main__':
    main()