# to build app
from fastapi import FastAPI
# allows web team access to app
from fastapi.middleware.cors import CORSMiddleware
# allows for html rendering
from fastapi.responses import HTMLResponse
# for data handling
import pandas as pd
from fastapi.encoders import jsonable_encoder
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

@app.get("/try0")
async def try0():
  return jsonable_encoder(pd.read_json("try0.json"))

@app.get("/markets/", response_model=List[schemas.Market])
def read_markets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    markets = crud.get_markets(db, skip=skip, limit=limit)
    return markets
    
@app.get("/markets_by_country_code/{country_code}", response_model=List[schemas.Market])
def markets_by_country_code(country_code: str = "UGA", db: Session = Depends(get_db)):
    markets = crud.get_markets_by_country_code(db, country_code=country_code)
    if markets is None:
        raise HTTPException(status_code=404, detail="Country Code not Recognized")
    return markets

@app.get("/market_by_name/{market_name}", response_model=schemas.Market)
def market_by_name(market_name: str = "Kiboga", db: Session = Depends(get_db)):
    market = crud.get_market_by_name(db, market_name=market_name)
    if market is None:
        raise HTTPException(status_code=404, detail="Name not Recognized")
    return market


# @app.get("/qc_wholesale/", response_model=schemas.QCWholesale)
# def qc_wholesale(db: Session = Depends(get_db)):
#   qc_table = crud.get_qc_wholesale(db)
#   #return qc_table
#   return {"message": "Under Construction"}

@app.get("/qc_wholesale_dummy")
async def qc_wholesale_dummy():
  qc_ws = pd.read_csv("qc_wholesale.csv")
  qc_ws = qc_ws.to_json()
  return qc_ws