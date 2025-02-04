from fastapi import APIRouter, HTTPException
from fastapi.params import Body
from config.database import get_connection
from pydantic import BaseModel, EmailStr, Field

router = APIRouter()

class CreateContact(BaseModel):
    name : str = Field(min_length=2, max_length=50)
    company_id : int
    email : EmailStr = Field(min_length=3, max_length=50)
    phone : str = Field(min_length=10, max_length=50)

class SearchContact(BaseModel):
    name : str = Field(min_length=2, max_length=50)

class DeleteContact(BaseModel):
    email : EmailStr = Field(min_length=2, max_length=50)
    phone : str = Field(min_length=3, max_length=50)

@router.get("/get_all_contacts")
async def get_contact():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT contacts.name, contacts.phone, contacts.email, companies.name AS company_name, companies.created_at FROM contacts LEFT JOIN companies ON contacts.company_id = companies.id")

        get_contacts = cursor.fetchall()

        cursor.close()
        conn.close()

        return get_contacts

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("search_contact")
async def search_contacts(search: SearchContact):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        query = "SELECT contacts.name, contacts.phone, contacts.email, companies.name FROM contacts LEFT JOIN companies ON contacts.company_id = companies.id WHERE companies.name = %s"
        values = (search.name, )

        cursor.execute(query, values)
        search_contact = cursor.fetchall()

        cursor.close()
        conn.close()

        return search_contact

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/add_contact")
async def create_contact(contacts: CreateContact):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        query = "INSERT INTO contacts (name, company_id, email, phone) VALUES (%s, %s, %s, %s)"
        values = (contacts.name, contacts.company_id, contacts.email, contacts.phone)

        cursor.execute(query, values)
        conn.commit()
        new_id = cursor.lastrowid
        cursor.execute("SELECT * FROM contacts WHERE id = %s", (new_id,))
        create_contacts = cursor.fetchone()

        cursor.close()
        conn.close()

        return create_contacts

    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/update_contact/{contacts_id}")
async def update_contact(contacts_id: int, contacts: CreateContact ):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM contacts WHERE id = %s", (contacts_id,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="Contact non trouvé")

        query = "UPDATE contacts SET name = %s, company_id = %s, email = %s, phone = %s WHERE id = %s"
        values = (contacts.name, contacts.company_id, contacts.email, contacts.phone, contacts_id)

        cursor.execute(query, values)
        conn.commit()

        cursor.execute ("SELECT * FROM contacts WHERE id = %s", (contacts_id,))
        update_contacts = cursor.fetchone()

        cursor.close()
        conn.close()

        return update_contacts

    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/delete_contact/{contacts_id}")
async def delete_contact(contacts_id: int, contacts: DeleteContact ):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM contacts WHERE id = %s", (contacts_id,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="Contact non trouvé")

        query = "DELETE FROM contacts WHERE email = %s AND phone = %s"
        values = (contacts.email, contacts.phone)

        cursor.execute(query, values)
        conn.commit()

        cursor.execute("SELECT * FROM contacts")

        delete_contacts = cursor.fetchall()

        cursor.close()
        conn.close()

        return delete_contacts

    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))