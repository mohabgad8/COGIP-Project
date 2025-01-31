from fastapi import FastAPI
from routes.companies_routes import router as companies_router
from routes.contacts_routes import router as contacts_router
from routes.invoices_routes import router as invoices_router

app = FastAPI()


app.include_router(
    companies_router,
    prefix="/companies"
)

app.include_router(
    contacts_router,
    prefix="/contacts"
)

app.include_router(
    invoices_router,
    prefix="/invoices"
)

@app.get("/")
async def root():
    return {"message": "Hello World"}