from fastapi import APIRouter, HTTPException
from config.database import get_connection
from pydantic import BaseModel, EmailStr, Field

router = APIRouter()

conn = get_connection()
cursor = conn.cursor(dictionary=True)

class CreateContact(BaseModel):
    name : str = Field(min_length=2, max_length=50)
    company_name : str = Field(min_length=2, max_length=50)
    email : EmailStr = Field(min_length=3, max_length=50)
    phone : str = Field(min_length=10, max_length=50)

class DeleteContact(BaseModel):
    email : EmailStr = Field(min_length=2, max_length=50)
    phone : str = Field(min_length=3, max_length=50)


@router.get("/get_all_companies")
async def get_all_companies():
    try:
        
        cursor.execute("SELECT id, name FROM companies")
        companies_list = cursor.fetchall()

        if not companies_list:
            raise HTTPException(status_code=404, detail="Aucune entreprise trouvée")

        companies_clean = [{"id": c[0], "name": c[1]} for c in companies_list]


        return companies_clean  

    except Exception as e:
        print(f"🔥 Erreur dans get_all_companies: {e}")
        raise HTTPException(status_code=500, detail=str(e))





@router.get("/get_all_contacts")
async def get_contact():
    try:
        
        cursor.execute("SELECT contacts.name, contacts.phone, contacts.email, companies.name AS company_name, companies.created_at FROM contacts LEFT JOIN companies ON contacts.company_id = companies.id ORDER BY contacts.created_at DESC")

        get_contacts = cursor.fetchall()

        cursor.close()
        conn.close()

        return get_contacts

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_all_contacts")
async def get_contact():
    try:
        cursor.execute("SELECT c.id, c.name, c.email, c.phone, co.name AS company_name FROM contacts c JOIN companies co ON c.company_id = co.id")

        contacts_list = cursor.fetchall()

        if not contacts_list:
            raise HTTPException(status_code=400, detail="Contact introuvable")

        return [{"id":c[0], "name":c[1], "email": c[2], "phone": c[3], "company_name": c[4]}
                for c in contacts_list]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_contact/{contact_name}")
async def get_contact(contact_name: str):
    try:
     
        query = "SELECT contacts.name, contacts.phone, contacts.email, companies.name AS company_name FROM contacts LEFT JOIN companies ON contacts.company_id = companies.id WHERE contacts.name = %s"
        values = (contact_name, )

        cursor.execute(query, values)
        search_contact = cursor.fetchall()

        return search_contact

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_last_contacts")
async def get_last_contacts():
    try:
        cursor.execute("SELECT contacts.name, contacts.phone, contacts.email, companies.name AS company_name, companies.created_at FROM contacts LEFT JOIN companies ON contacts.company_id = companies.id ORDER BY created_at DESC LIMIT 5")

        get_last_contact = cursor.fetchall()

        return get_last_contact

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@router.post("/add_contact")
async def create_contact(contacts: CreateContact):
    try:
       
        query = "SELECT id FROM companies WHERE TRIM(LOWER(name)) = TRIM(LOWER(%s))"
        values = (contacts.company_name,)
        cursor.execute(query, values)

        company_id_result = cursor.fetchone()
       
        if not company_id_result:
            raise HTTPException(status_code=400, detail=f"Entreprise '{contacts.company_name}' introuvable")

        
        if company_id_result is None or len(company_id_result) == 0:
            raise HTTPException(status_code=500, detail="Erreur: company_id introuvable après la requête SQL.")

        company_id = company_id_result['id']
        
        sql_query = "INSERT INTO contacts (name, company_id, email, phone) VALUES (%s, %s, %s, %s)"
        sql_values = (contacts.name, company_id, contacts.email, contacts.phone)

        
        cursor.execute(sql_query, sql_values)
        conn.commit()

        new_id = cursor.lastrowid
        cursor.execute("SELECT * FROM contacts WHERE id = %s", (new_id,))
        create_contacts = cursor.fetchone()

        return create_contacts

    except Exception as e:
        conn.rollback()
        error_message = str(e)
        print(f"FULL SQL ERROR: {error_message}")  
        raise HTTPException(status_code=500, detail=f"SQL Error: {error_message}")


@router.put("/update_contact/{contacts_id}")
async def update_contact(contacts_id: int, contacts: CreateContact ):
    try:
        cursor.execute("SELECT * FROM contacts WHERE id = %s", (contacts_id,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="Contact non trouvé")

        query = "UPDATE contacts SET name = %s, company_id = %s, email = %s, phone = %s WHERE id = %s"
        values = (contacts.name, contacts.company_id, contacts.email, contacts.phone, contacts_id)

        cursor.execute(query, values)
        conn.commit()

        cursor.execute ("SELECT * FROM contacts WHERE id = %s", (contacts_id,))
        update_contacts = cursor.fetchone()

        return update_contacts

    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/delete_contact/{contacts_id}")
async def delete_contact(contacts_id: int, contacts: DeleteContact ):
    try:
        cursor.execute("SELECT * FROM contacts WHERE id = %s", (contacts_id,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="Contact non trouvé")

        query = "DELETE FROM contacts WHERE email = %s AND phone = %s"
        values = (contacts.email, contacts.phone)

        cursor.execute(query, values)
        conn.commit()

        cursor.execute("SELECT * FROM contacts")

        delete_contacts = cursor.fetchall()

        return delete_contacts

    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    

    