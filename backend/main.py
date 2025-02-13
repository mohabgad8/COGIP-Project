from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.types_routes import router as types_router
from routes.companies_routes import router as companies_router
from routes.contacts_routes import router as contacts_router
from routes.invoices_routes import router as invoices_router
from routes.users_routes import router as users_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    companies_router,
    # prefix="/companies"
)

app.include_router(
    contacts_router,
    # prefix="/contacts"
)

app.include_router(
    invoices_router,
    # prefix="/invoices"
)

app.include_router(
    users_router,
    # prefix="/users"
)

app.include_router(
    types_router,
    # prefix="/users"
)

@app.get("/")
async def root():
    return {"message": "Hello World"}