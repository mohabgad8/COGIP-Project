from fastapi import APIRouter, HTTPException
from config.database import get_connection

router = APIRouter()


@router.get("/")

async def get_invoices():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM invoices")
        invoices = cursor.fetchall()
        cursor.close()
        conn.close()
        return invoices
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))