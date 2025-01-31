from fastapi import APIRouter, HTTPException
from config.database import get_connection

router = APIRouter()


@router.get("/")

async def get_contacts():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM contacts")
        contacts = cursor.fetchall()
        cursor.close()
        conn.close()
        return contacts
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))