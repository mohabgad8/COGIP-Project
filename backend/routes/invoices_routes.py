from fastapi import APIRouter, HTTPException
from config.database import get_connection
from pydantic import BaseModel, Field
from datetime import datetime, date


router = APIRouter()

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
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        query = "SELECT invoices.ref, invoices.date_due, companies.name AS company_name, invoices.created_at FROM invoices LEFT JOIN companies ON invoices.id_company = companies.id WHERE invoices.ref = %s"
        values = (ref_invoice,)

        cursor.execute(query, values)

        get_one_invoice = cursor.fetchone()

        cursor.close()
        conn.close()

        return get_one_invoice

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_all_invoices")
async def get_invoices():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT invoices.ref, invoices.date_due, invoices.created_at, companies.name FROM invoices LEFT JOIN companies ON invoices.id_company = companies.id ORDER BY created_at DESC")

        get_invoice = cursor.fetchall()

        cursor.close()
        conn.close()

        return get_invoice

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/search_invoice")
async def search_invoices(search: SearchInvoices):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        query = "SELECT invoices.ref, invoices.date_due, companies.name, invoices.created_at FROM invoices LEFT JOIN companies ON invoices.id_company = companies.id WHERE companies.name = %s"
        values = (search.companies.name, )

        cursor.execute(query, values)
        search_invoice = cursor.fetchall()

        cursor.close()
        conn.close()

        return search_invoice

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_last_invoices")
async def get_last_invoices():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT invoices.ref, invoices.date_due, invoices.created_at, companies.name FROM invoices LEFT JOIN companies ON invoices.id_company = companies.id ORDER BY created_at DESC LIMIT 5")

        get_last_invoice = cursor.fetchall()

        cursor.close()
        conn.close()

        return get_last_invoice

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_last_invoices_company/{company_name}")
async def get_last_invoices_company(company_name : str):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        query = "SELECT invoices.ref, invoices.date_due, invoices.created_at, companies.name AS company_name FROM invoices LEFT JOIN companies ON invoices.id_company = companies.id WHERE companies.name = %s ORDER BY created_at DESC LIMIT 5"
        values = (company_name,)

        cursor.execute(query, values)

        get_last_invoice_company = cursor.fetchall()

        cursor.close()
        conn.close()

        return get_last_invoice_company

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/add_invoice")
async def create_invoices(invoices: InvoicesVerify ):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        query = "INSERT INTO invoices (date_due, id_company, ref) VALUES (%s, %s, %s)"
        values = (invoices.date_due, invoices.id_company, None)

        cursor.execute(query, values)
        conn.commit()

        new_id = cursor.lastrowid
        date_part = datetime.strptime(invoices.date_due, "%Y-%m-%d").strftime("%Y%m%d")
        invoice_ref = f"F{date_part}-{new_id:04d}"

        update_query ="UPDATE invoices SET ref = %s where invoices.id = %s"
        values = (invoice_ref, new_id,)
        cursor.execute(update_query, values)
        conn.commit()


        cursor.execute("SELECT * FROM invoices WHERE ref = %s", (invoice_ref,))
        create_invoice = cursor.fetchone()

        cursor.close()
        conn.close()

        return create_invoice

    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/update_invoice/{date_due}")
async def update_invoices(date_due: date, invoices: InvoicesVerify ):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM invoices WHERE date_due = %s", (date_due,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="Facture non trouvé")

        query = "UPDATE invoices SET ref = %s, id_company = %s WHERE date_due = %s"
        values = (invoices.ref, invoices.id_company, date_due)

        cursor.execute(query, values)
        conn.commit()

        cursor.execute ("SELECT * FROM invoices WHERE date_due = %s", (date_due,))
        update_invoice = cursor.fetchone()

        cursor.close()
        conn.close()

        return update_invoice

    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/delete_invoice/{date_due}")
async def delete_invoice(date_due: date, invoices: DeleteInvoices):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM invoices WHERE date_due = %s", (date_due,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="Contact non trouvé")

        query = "DELETE FROM invoices WHERE ref = %s"
        values = (invoices.ref,)

        cursor.execute(query, values)
        conn.commit()

        cursor.execute("SELECT * FROM invoices")

        delete_invoices = cursor.fetchall()

        cursor.close()
        conn.close()

        return delete_invoices

    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))