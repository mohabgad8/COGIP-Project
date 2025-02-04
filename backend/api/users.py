from fastapi import APIRouter, HTTPException
from fastapi.params import Body
from core.database import get_connection

router = APIRouter()



@router.get("/get_user")

async def get_users():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        cursor.close()
        conn.close()
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@router.post("/add_user")

async def create_users(users: dict = Body(...) ):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "INSERT INTO users (first_name, role_id, last_name, email, password) VALUES (%s, %s, %s, %s, %s)"
        values = (users['first_name'], users['role_id'], users['last_name'], users['email'], users['password'])

        cursor.execute(query, values)
        conn.commit()
        users = cursor.fetchall()
        cursor.close()
        conn.close()
        return users

    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))


