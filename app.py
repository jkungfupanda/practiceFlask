from flask import Flask, jsonify, render_template, request
import mysql.connector
from password import *

app = Flask(__name__)

# Closing database connection
def close_database_connection(cursor, cnx):
    if cursor:
        cursor.close()
    if cnx:
        cnx.close()

@app.route('/')
def get_users():
    return render_template('index.html')

@app.route('/users/query', methods=['POST'])
def query_users():
    cnx = None
    try:
        # Connecting to the MySQL database
        cnx = mysql.connector.connect(user='root', password=psd,
                                      host='localhost', database='my_database')

        # Creating a cursor object to execute SQL queries
        cursor = cnx.cursor(dictionary=True)

        # Querying the entire table
        query = "SELECT * FROM sampledata"
        cursor.execute(query)

        # Fetching all the rows and returning as JSON
        rows = cursor.fetchall()
    except mysql.connector.Error as error:
        print(f"Failed to get record from MySQL table: {error}")

    finally:
        # Closing database connection
        close_database_connection(cursor, cnx)

    return jsonify(success=True, error=0, data=rows)

@app.route('/employee/new', methods=['POST'])
def new_employee():
    cnx = None
    try:
        # Connecting to the MySQL database
        cnx = mysql.connector.connect(user='root', password=psd,
                                      host='localhost', database='my_database')

        # Creating a cursor object to execute SQL queries
        cursor = cnx.cursor()

        # Retrieving the employee data from the HTML form
        name = request.form['name']
        employee_id = request.form['id']

        # Inserting the employee data into the database
        query = f"INSERT INTO employees (name, id) VALUES ('{name}', '{employee_id}')"
        cursor.execute(query)

        # Committing the transaction
        cnx.commit()
    except mysql.connector.Error as error:
        print(f"Failed to insert record into MySQL table: {error}")
        cnx.rollback()

    finally:
        # Closing database connection
        close_database_connection(cursor, cnx)

    return jsonify(success=True, error=0)

@app.route('/employee/lookup', methods=['POST'])
def lookup_employee():
    cnx = None
    try:
        # Connecting to the MySQL database
        cnx = mysql.connector.connect(user='root', password=psd,
                                      host='localhost', database='my_database')

        # Creating a cursor object to execute SQL queries
        cursor = cnx.cursor()

        # Retrieving the employee ID from the HTML form
        employee_id = request.form['employee_id']

        # Querying the employee data from the database
        query = f"SELECT * FROM employees WHERE id = '{employee_id}'"
        cursor.execute(query)

        # Fetching the employee data and returning as JSON
        row = cursor.fetchone()
        if row:
            employee = {'name': row[0], 'id': row[1]}
            return jsonify(success=True, error=0, data=employee)
        else:
            return jsonify(success=True, error=1, message='Employee not found')
    except mysql.connector.Error as error:
        print(f"Failed to get record from MySQL table: {error}")

    finally:
        # Closing database connection
        close_database_connection(cursor, cnx)

    return jsonify(success=False, error=2, message='An error occurred')


if __name__ == '__main__':
    # Running Flask app on port 8000
    app.run(debug=True, port=8000)
