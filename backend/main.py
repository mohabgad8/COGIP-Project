from fastapi import FastAPI
from routes.companies_routes import router as companies_router

app = FastAPI()


app.include_router(
    companies_router,
    prefix="/companies"
)

@app.get("/")
async def root():
    return {"message": "Hello World"}