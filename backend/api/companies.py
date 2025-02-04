from fastapi import APIRouter, HTTPException
from core.database import get_connection

router = APIRouter()


@router.get("/")

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
