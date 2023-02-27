# from flask import Flask, jsonify
# import mysql.connector

# app = Flask(__name__)

# @app.route('/')
# def get_data():
#     # Connect to the database
#     cnx = mysql.connector.connect(user='localhost', password='Attackonhunterdeadman',
#                                   host='localhost', database='my_database')
    
#     # Execute a query to fetch all data from the `sampledata` table
#     cursor = cnx.cursor()
#     query = "SELECT * FROM sampledata"
#     cursor.execute(query)
#     rows = cursor.fetchall()
    
#     # Convert the data to a list of dictionaries and return as JSON
#     data = []
#     for row in rows:
#         data.append({'id': row[0], 'name': row[1]})
#     return jsonify(data)

# if __name__ == '__main__':
#     app.run()