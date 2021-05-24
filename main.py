import uvicorn

from fastapi import FastAPI

from routes import production

from database.main import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(debug=True)

# app.include_router(qualities.router)
app.include_router(production.router)

if __name__ == '__main__':
    uvicorn.run(app="main:app", host="0.0.0.0", port=8001, log_level='info', reload=True)
