import mysql.connector

def test_database_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Attackonhunterdeadman",
            database="my_database"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sampledata")
        results = cursor.fetchall()
        print(results)
        cursor.close()
        conn.close()
    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

test_database_connection()
