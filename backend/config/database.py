import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    try:
        mydb = mysql.connector.connect(
            database=os.getenv("DB_NAME"),
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=int(os.getenv("DB_PORT")),
            charset="utf8mb4",
            collation="utf8mb4_general_ci"
        )
        return mydb
    except mysql.connector.Error as err:
        print("Erreur de connexion à la base de données:", err)
        return None