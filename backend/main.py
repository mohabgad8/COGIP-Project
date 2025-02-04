from fastapi import FastAPI
from api.companies import router as companies_router
from api.contacts import router as contacts_router
from api.invoices import router as invoices_router
from api.users import router as users_router
app = FastAPI()

app.include_router(
    companies_router,
)

app.include_router(
    contacts_router,
)

app.include_router(
    invoices_router,
)

app.include_router(
    users_router,
)

@app.get("/")
async def root():
    return {"message": "Hello World"}




