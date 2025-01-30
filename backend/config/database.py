import mysql.connector
import os
from tabulate import tabulate
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
    cursor.execute("SELECT * FROM companies")
    result = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    if result:
        print("Database connection established")
        print("Result:\n",tabulate(result,headers=columns,tablefmt='fancy_grid'))

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