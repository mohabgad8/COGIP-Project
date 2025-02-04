from fastapi import APIRouter, HTTPException
from config.database import get_connection

router = APIRouter()


@router.get("/get_companies")

async def get_companies():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM companies")
        companies = cursor.fetchall()
        cursor.close()
        conn.close()
        return companies
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
