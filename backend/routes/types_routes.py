from fastapi import APIRouter, HTTPException
from config.database import get_connection
from pydantic import BaseModel, Field
from datetime import datetime, date
import uuid

router = APIRouter()

conn = get_connection()
cursor = conn.cursor(dictionary=True)

class TypesVerify(BaseModel):
    ref_id : int

@router.get("/get_all_types")
async def get_all_types():
    try:
        cursor.execute("SELECT name FROM types")  
        types_list = cursor.fetchall()

        if not types_list:
            raise HTTPException(status_code=404, detail="Aucun type trouvé")

        type_names = [t["name"] for t in types_list]  
        return type_names  

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
