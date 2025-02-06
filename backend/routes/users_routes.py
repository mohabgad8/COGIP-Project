import re
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel, EmailStr, validator, field_validator
from config.database import get_connection, hash_password, verify_password

router = APIRouter()
db = get_connection()
cursor = db.cursor(dictionary=True)

class User(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str

    @field_validator("password")
    def validate_password(cls, value: str) -> str:

        errors = []

        if len(value) < 10:
            errors.append("10 characters")
        if not re.search(r"\d", value):
            errors.append("a number")
        if not re.search(r"[@$!%*?&]", value):
            errors.append("a special character")

        if errors:
            raise ValueError(f"Password must contain at least {', '.join(errors)}.")

        return value



class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class DeleteUser(BaseModel):
    email: EmailStr

@router.post("/add_user")
async def add_user(users: User):
    try:
        hashed_password = hash_password(users.password)
        query = "INSERT INTO users (first_name, last_name,email, password) VALUES (%s, %s, %s, %s)"
        values = (users.first_name, users.last_name, users.email, hashed_password)

        cursor.execute(query, values)
        db.commit()

        return {"message" : "User added successfully", "user_id" : cursor.lastrowid}

    except Exception as e:
        db.rollback()
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
            SET first_name = %s, last_name = %s, email = %s, password = %s
            WHERE id = %s
        """
        values = (user.first_name, user.last_name, user.email, hash_password(user.password), user_id)
        cursor.execute(query, values)
        db.commit()
        # verify if the user has been modified
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail = "User not found or no changes made")

        #Get modified user
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        updated_user = cursor.fetchone()
        return {"message" : "User updated successfully", "updated_user": updated_user}

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/delete_user")
async def delete_user(user: DeleteUser):
    try:
        query = "DELETE FROM users WHERE email = %s"
        values = (user.email,)
        cursor.execute(query, values)
        db.commit()

        # verify if the user has been deleted
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="User not found or no changes made")

        return {"message" : "User deleted successfully !"}

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/login")
async def login_user(required_user: LoginRequest):
    try:
        # Pre-condition : There are no email duplicates
        # Fetch required_user data from database
        query = "SELECT * FROM users WHERE email = %s "
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

    #test