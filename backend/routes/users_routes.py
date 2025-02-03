from fastapi.params import Body
from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel, EmailStr
from config.database import get_connection, hash_password, verify_password

router = APIRouter()
conn = get_connection()
cursor = conn.cursor(dictionary=True)

class User(BaseModel):
    first_name: str
    role_id: int
    last_name: str
    email: EmailStr
    password: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

@router.post("/add_user")
async def add_user(users: User):
    try:
        hashed_password = hash_password(users.password)
        query = "INSERT INTO users (first_name, role_id, last_name, email, password) VALUES (%s, %s, %s, %s, %s)"
        values = (users.first_name, users.role_id, users.last_name, users.email, hashed_password)

        cursor.execute(query, values)
        conn.commit()

        return {"message" : "User added successfully", "user_id" : cursor.lastrowid}

    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/get_user")
async def get_user():
    try:
        query = "SELECT * FROM users"
        cursor.execute(query)
        users = cursor.fetchall()

        return {"users": users}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/update_user/{user_id}")
async def update_user(user_id: int, user: User):
    try:
        query = """
            UPDATE users
            SET first_name = %s, last_name = %s, email = %s, password = %s, role_id = %s
            WHERE id = %s
        """
        values = (user.first_name, user.last_name, user.email, user.password, user.role_id, user_id)
        cursor.execute(query, values)
        conn.commit()
        # verify if the user has been modified
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail = "User not found or no changes made")

        #Get modified user
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        updated_user = cursor.fetchone()
        return {"message" : "User updated successfully", "updated_user": updated_user}

    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/delete_user")
async def delete_user():
    try:
        query = "DELETE FROM users WHERE first_name = {first_name}"
        cursor.execute(query)
        conn.commit()

    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/login")
async def login_user(required_user: LoginRequest):
    try:
        # Pre-condition : There are no email duplicates
        # Fetch required_user data from database
        query = "SELECT * FROM users WHERE email = %s"
        values = (required_user.email,)
        cursor.execute(query, values)
        db_user = cursor.fetchone()

        # Verify if user exists in database
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found, try again")

        # Verify if password corresponds
        stored_password_hex = db_user['password']
        if verify_password(required_user.password, stored_password_hex):
            return {"message" : "Login successful !"}
        else: raise HTTPException(status_code=401, detail="Invalid password, try again")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))