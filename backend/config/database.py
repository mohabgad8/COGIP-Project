import mysql.connector
import os
import bcrypt
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

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.hex()

def verify_password(password: str, hashed_password_hex: str) -> bool:
    # Convert hex to bytes -> because bcrypt checks pw in bytes and not in hex
    hashed_password_bytes = bytes.fromhex(hashed_password_hex)
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password_bytes)