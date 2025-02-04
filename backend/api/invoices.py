from fastapi import APIRouter, HTTPException
from fastapi.params import Body
from core.database import get_connection

router = APIRouter()


@router.get("/get_invoices")

async def get_invoices():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM invoices")

        get_invoice = cursor.fetchall()

        cursor.close()
        conn.close()

        return get_invoice

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/add_invoice")

async def create_invoices(invoices: dict = Body(...) ):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        query = "INSERT INTO invoices (ref, id_company) VALUES (%s, %s)"
        values = (invoices['ref'], invoices['id_company'])

        cursor.execute(query, values)
        conn.commit()

        create_invoice = cursor.fetchall()

        cursor.close()
        conn.close()

        return create_invoice

    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))



@router.put("/update_invoice/{invoice_id}")

async def update_invoices(invoice_id: int, invoices: dict = Body(...) ):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM invoices WHERE id = %s", (invoice_id,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="Facture non trouvé")

        query = "UPDATE invoices SET ref = %s WHERE id = %s"
        values = (invoices['ref'], invoice_id)

        cursor.execute(query, values)
        conn.commit()

        cursor.execute ("SELECT * FROM invoices WHERE id = %s", (invoice_id,))
        update_invoice = cursor.fetchone()

        cursor.close()
        conn.close()

        return update_invoice

    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/delete_invoice/{invoice_id}")
async def delete_invoice(invoice_id: int, invoices: dict = Body(...) ):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM invoices WHERE id = %s", (invoice_id,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="Contact non trouvé")

        query = "DELETE FROM invoices WHERE ref = %s"
        values = (invoices['ref'],)

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
