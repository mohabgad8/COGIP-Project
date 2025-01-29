import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

try:
    mydb = mysql.connector.connect(
        database=os.getenv("DB_NAME"),
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=int(os.getenv("DB_PORT"))
    )

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchone()

    if result:
        print("Database connection established")
        print("Server version: ")
        print("Result: ", result)

except mysql.connector.Error as err:
    print("Failed to connect to MySQL database")
    print(f"Error: {err}")
    print("Error info: ", err.args)

# finally:
#     if 'mydb' in locals():
#         if mydb.is_connected():
#             mydb.close()
#             print("Database closed")
#         else:
#             print("Connection was not established")