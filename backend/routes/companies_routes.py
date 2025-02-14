from fastapi import APIRouter, HTTPException
from config.database import get_connection
from pydantic import BaseModel

router = APIRouter()
db = get_connection()
cursor = db.cursor(dictionary = True)


class NewCompany(BaseModel):
    name: str
    type: str
    country: str
    tva: str

class UpdatedCompany(BaseModel):
    name: str
    type_id: int
    country: str
    tva: str

class DeleteCompany(BaseModel):
    name: str

# get all companies' infos
@router.get("/get_company/{company_name}")
async def get_company(company_name: str):
    try:
        # get required_company's infos + type
        query = """
            SELECT  companies.name, companies.country, companies.tva, types.name AS type
            FROM companies
            LEFT JOIN types ON companies.type_id = types.id
            WHERE companies.name = %s
        """
        values = (company_name,)
        cursor.execute(query, values)
        fetched_company = cursor.fetchall()

        return fetched_company

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#get_
@router.get("/get_last5_companies")
async def get_last5_companies():
    try:
        query = """
            SELECT companies.name, companies.tva, companies.country, types.name AS type, companies.created_at
            FROM companies
            LEFT JOIN types ON companies.type_id = types.id
            ORDER BY created_at DESC
            LIMIT 5
        """
        cursor.execute(query)
        last5_companies = cursor.fetchall()

        return last5_companies

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_all_companies")
async def get_all_companies():
    try:
        query = """
            SELECT companies.name, companies.tva, companies.country, types.name AS type, companies.created_at
            FROM companies
            LEFT JOIN types on companies.type_id = types.id
            ORDER BY companies.name
        """
        cursor.execute(query)
        all_companies = cursor.fetchall()

        return all_companies

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/add_company")
async def add_company(new_company: NewCompany):
    try:
        query = "SELECT id FROM types WHERE TRIM(LOWER(name)) = TRIM(LOWER(%s))"
        cursor.execute(query, (new_company.type,))
        type_id_result = cursor.fetchone()

        if not type_id_result:
            raise HTTPException(status_code=400, detail=f"Type '{new_company.type}' introuvable")

        type_id = type_id_result['id'] 
        sql_query = "INSERT INTO companies (name, type_id, country, tva) VALUES (%s, %s, %s, %s)"
        sql_values = (new_company.name, type_id, new_company.country, new_company.tva)

        cursor.execute(sql_query, sql_values)
        db.commit()

        return {"message": "Company added successfully", "company_id": cursor.lastrowid}

    except Exception as e:
        db.rollback()
        error_message = str(e)
        raise HTTPException(status_code=500, detail=f"SQL Error: {error_message}")



@router.put("/update_company/{company_id}")
async def update_company(company_id: int, required_company: UpdatedCompany):
    try:
        query = """
            UPDATE companies
            SET name = %s, country = %s, tva = %s, type_id = %s
            WHERE id = %s
        """
        values = (required_company.name, required_company.country, required_company.tva, required_company.type_id, company_id)
        cursor.execute(query, values)
        db.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Company not found or no changes made")

        # Get modified company
        cursor.execute("SELECT * FROM companies WHERE id = %s", (company_id,))
        updated_company = cursor.fetchone()
        return {"message": "User updated successfully", "updated_user": updated_company}

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/delete_company")
async def delete_company(company: DeleteCompany):
    try:
        query = "DELETE FROM companies WHERE name = %s"
        values = (company.name,)
        cursor.execute(query, values)
        db.commit()

        # verify if the company has been deleted
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Company not found or no changes made")

        return {"message" : "Company deleted successfully !"}

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/get_type_for_dashboard")
async def get_all_types():
    try:
        print("🔍 Fetching types from database...")
        cursor.execute("SELECT name FROM types")
        types_list = cursor.fetchall()

        if not types_list:
            raise HTTPException(status_code=404, detail="Aucun type trouvé")

        types_clean = [t[0] if isinstance(t, tuple) else t['name'] for t in types_list]
        print(f"✅ Types trouvés: {types_clean}")

        return types_clean  

    except Exception as e:
        print(f"🔥 Erreur dans get_all_types: {e}")
    raise HTTPException(status_code=500, detail=str(e))
