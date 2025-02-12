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

@router.get("/get_types/{ref_id}")
async def get_types(ref_id: TypesVerify):
    try:
        cursor.execute("SELECT types.name FROM types WHERE id = %s", (ref_id,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="Type non trouvée")

        query = "SELECT types.name FROM types WHERE id = %s"
        values = (ref_id,)

        cursor.execute(query, values)

        get_one_type = cursor.fetchone()

        return get_one_type

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))