from fastapi import APIRouter, HTTPException
from config.database import get_connection
from pydantic import BaseModel, EmailStr

router = APIRouter()
connection = get_connection()
cursor = connection.cursor(dictionary = True)

class CompanySearch(BaseModel):
    name: str

# get all companies' infos
@router.get("/get_company")
async def get_company(company: CompanySearch):
    try:
        query = """
            SELECT * FROM companies
            INNER JOIN types ON companies.type_id = types.id
        """
        cursor.execute(query)
        companies = cursor.fetchall()

        return {"companies" : companies}
    except Exception as e:
        raise HTTPException(status_code=404, detail="Data not found")