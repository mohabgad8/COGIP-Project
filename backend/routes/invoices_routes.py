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
async def create_invoices(invoices: InvoicesVerify):
    try:
        query = "INSERT INTO invoices (date_due, id_company) VALUES (%s, %s)"
        values = (invoices.date_due, invoices.id_company,)
        cursor.execute(query, values)
        conn.commit()

        new_id = cursor.lastrowid

        date_part = datetime.strptime(invoices.date_due, "%Y-%m-%d")

        ref_date = date_part.strftime("%Y%m%d")

        invoice_ref = f"F{ref_date}-{new_id:03d}"

        u_query ="UPDATE invoices SET ref = %s where invoices.id = %s"
        values = (invoice_ref, new_id,)
        cursor.execute(u_query, values)
        conn.commit()

        query = "SELECT * FROM invoices WHERE ref = %s"
        values = (invoice_ref,)
        cursor.execute (query, values)

        create_invoice = cursor.fetchone()

        return create_invoice

    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))


# @router.post("/add_invoice")
# async def create_invoices(invoices: InvoicesVerify):
#     try:
#         #strptime (string parse time) sert à convertir une string en objet dateime
#         date_due = datetime.strptime(invoices.date_due, "%Y-%m-%d")
#
#         #strftime (string fomat time) sert à convertir un objet datetime en une string
#         ref_date = date_due.strftime('%Y%m%d')
#
#         uuid_ref = f"F{ref_date}-{str(uuid.uuid4())[:32]}"
#
#         query = "INSERT INTO invoices (date_due, id_company, ref) VALUES (%s, %s, %s)"
#         values = (invoices.date_due, invoices.id_company, uuid_ref)
#
#         cursor.execute(query, values)
#         conn.commit()
#
#         query = "SELECT * FROM invoices WHERE ref = %s"
#         cursor.execute(query, (uuid_ref,))
#         created_invoice = cursor.fetchone()
#
#         return created_invoice
#
#     except Exception as e:
#         conn.rollback()
#         raise HTTPException(status_code=500, detail=str(e))

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