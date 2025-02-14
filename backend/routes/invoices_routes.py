from fastapi import APIRouter, HTTPException
from config.database import get_connection
from pydantic import BaseModel, Field
from datetime import datetime, date
import uuid

router = APIRouter()

conn = get_connection()
cursor = conn.cursor(dictionary=True)

class InvoicesVerify(BaseModel):
    date_due : str = Field(min_length=2, max_length=50)
    id_company : int

class SearchInvoices(BaseModel):
    company_name: str = Field(min_length=2, max_length=50)

class DeleteInvoices(BaseModel):
    ref : str = Field(min_length=2, max_length=50)

class GetInvoice(BaseModel):
    ref : str = Field(min_length=2, max_length=50)

class GetAllInvoices(BaseModel):
    ref: str = Field(min_length=2, max_length=50)
    created_at: datetime = Field(default_factory=datetime.now)
    company_name: str = Field(min_length=2, max_length=50)

    class Config:
        from_attribute = True


@router.get("/get_invoice/{ref_invoice}")
async def get_invoice(ref_invoice: str):
    try:
        cursor.execute("SELECT * FROM invoices WHERE ref = %s", (ref_invoice,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="Facture non trouvée")

        query = "SELECT invoices.ref, invoices.date_due, companies.name AS company_name, invoices.created_at FROM invoices LEFT JOIN companies ON invoices.id_company = companies.id WHERE invoices.ref = %s"
        values = (ref_invoice,)

        cursor.execute(query, values)

        get_one_invoice = cursor.fetchone()

        return get_one_invoice

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_all_invoices")
async def get_invoices():
    try:
        cursor.execute("SELECT invoices.ref, invoices.date_due, invoices.created_at, companies.name FROM invoices LEFT JOIN companies ON invoices.id_company = companies.id ORDER BY created_at DESC")

        get_invoice = cursor.fetchall()

        return get_invoice

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/search_invoice")
async def search_invoices(search: SearchInvoices):
    try:
        query = "SELECT invoices.ref, invoices.date_due, companies.name, invoices.created_at FROM invoices LEFT JOIN companies ON invoices.id_company = companies.id WHERE companies.name = %s"
        values = (search.companies.name, )

        cursor.execute(query, values)
        search_invoice = cursor.fetchall()

        return search_invoice

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_last_invoices")
async def get_last_invoices():
    try:
        cursor.execute("SELECT invoices.ref, invoices.date_due, invoices.created_at, companies.name FROM invoices LEFT JOIN companies ON invoices.id_company = companies.id ORDER BY created_at DESC LIMIT 5")

        get_last_invoice = cursor.fetchall()

        return get_last_invoice

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_last_invoices_company/{company_name}")
async def get_last_invoices_company(company_name : str):
    try:
        query = "SELECT invoices.ref, invoices.date_due, invoices.created_at, companies.name AS company_name FROM invoices LEFT JOIN companies ON invoices.id_company = companies.id WHERE companies.name = %s ORDER BY created_at DESC LIMIT 5"
        values = (company_name,)
        cursor.execute(query, values)
        if not cursor.fetchall():
            raise HTTPException(status_code=404, detail="Entreprise non trouvée")

        query = "SELECT invoices.ref, invoices.date_due, invoices.created_at, companies.name AS company_name FROM invoices LEFT JOIN companies ON invoices.id_company = companies.id WHERE companies.name = %s ORDER BY created_at DESC LIMIT 5"
        values = (company_name,)

        cursor.execute(query, values)

        get_last_invoice_company = cursor.fetchall()

        return get_last_invoice_company

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/add_invoice")
async def add_invoice(invoice: dict):
    try:
      
        query = "SELECT id FROM companies WHERE LOWER(name) = LOWER(%s)"
        values = (invoice["company_name"],)
        cursor.execute(query, values)
        company_id_result = cursor.fetchone()
        id_company = company_id_result["id"]  
        today = datetime.today().strftime('%Y%m%d')

        query = "SELECT COUNT(*) AS total FROM invoices WHERE DATE(created_at) = CURDATE()"
        cursor.execute(query)
        count = cursor.fetchone()["total"] + 1
        ref = f"F{today}-{count:03d}"

        
        query = "INSERT INTO invoices (date_due, id_company, ref) VALUES (%s, %s, %s)"
        values = (invoice["due_date"], id_company, ref)
        cursor.execute(query, values)
        conn.commit()

        return {"message": "Facture ajoutée avec succès", "ref": ref}


    except Exception as e:
        conn.rollback()
        print(f"🔥 ERREUR INCONNUE : {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))




@router.put("/update_invoice/{invoice_ref}")
async def update_invoices(invoice_ref: str, invoices: InvoicesVerify ):
    try:
        cursor.execute("SELECT * FROM invoices WHERE ref = %s", (invoice_ref,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="Facture non trouvée")

        query = "UPDATE invoices SET ref = %s, id_company = %s WHERE ref = %s"
        values = (invoices.ref, invoices.id_company, invoice_ref)

        cursor.execute(query, values)
        conn.commit()

        cursor.execute ("SELECT * FROM invoices WHERE ref = %s", (invoice_ref,))
        update_invoice = cursor.fetchone()

        return update_invoice

    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/delete_invoice/{ref_invoice}")
async def delete_invoice(ref_invoice: str):
    try:
        cursor.execute("SELECT * FROM invoices WHERE ref = %s", (ref_invoice,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="Facture non trouvée")

        query = "DELETE FROM invoices WHERE ref = %s"
        values = (ref_invoice,)

        cursor.execute(query, values)
        conn.commit()

        cursor.execute("SELECT * FROM invoices")

        delete_invoices = cursor.fetchall()

        return delete_invoices

    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_total_invoices")
async def get_total_invoices():
    try:
        query = "SELECT COUNT(invoices.id) FROM invoices"
        cursor.execute(query)

        get_total_invoice = cursor.fetchall()

        return get_total_invoice

    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))