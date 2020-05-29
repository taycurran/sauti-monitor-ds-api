# to build app
from fastapi import FastAPI
# allows web team access to app
from fastapi.middleware.cors import CORSMiddleware
# allows for html rendering
from fastapi.responses import HTMLResponse
# for data handling
import pandas as pd

# imports for database
from typing import List
from . import crud, models, schemas 
from .database import SessionLocal, engine
from sqlalchemy.orm import Session 
from fastapi import Depends, HTTPException

# --- DB Models ---
models.Base.metadata.create_all(bind=engine)

# ------ Build App ------
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CORS - Cross-Origin Resource Sharing
# Gives Web Team Access to API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def root():
  """
  Sauti Market Monitor API  
  Verifies the API is deployed, and links to the docs.
  """
  return HTMLResponse("""
  <h1>Sauti Market Monitor</h1>
  <p>Go to <a href="/docs">/docs</a> for documentation.</p>
  """)

@app.get("/markets/", response_model=List[schemas.Market])
def read_markets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    markets = crud.get_market(db, skip=skip, limit=limit)
    return markets

@app.get("/product_raw_info/", response_model=List[schemas.ProductRawInfo])
def read_products_raw_info(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products_raw = crud.get_product_raw_info(db, skip=skip, limit=limit)
    return products_raw

@app.get("/qc_wholesale_dummy")
async def qc_wholesale_dummy():
  qc_ws = pd.read_csv("qc_wholesale.csv")
  qc_ws = qc_ws.to_json()
  return qc_ws