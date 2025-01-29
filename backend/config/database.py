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
        port=int(os.getenv("DB_PORT")),
        charset='utf8mb4',
        collation='utf8mb4_general_ci'
    )

    cursor = mydb.cursor()
    cursor.execute("SELECT 1")
    result = cursor.fetchone()

    if result:
        print("Database connection established")
        print("Result:", result)

except mysql.connector.Error as err:
    print("Failed to connect to MySQL database")
    print(f"Error: {err}")
    print("Error info:", err.args)

finally:
    if 'mydb' in locals():
        if mydb.is_connected():
            mydb.close()
            print("Database closed")
        else:
            print("Connection was not established")