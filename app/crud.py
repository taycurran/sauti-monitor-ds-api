# allows for declaration of the type of db parameters and 
# better type checks
from sqlalchemy.orm import Session
from . import models, schemas
# ----------------------------------------------------------------------------
def get_market_by_name(db: Session, market_name: str):
    return db.query(models.Markets).filter\
        (models.Markets.market_name == market_name).first()

def get_markets_by_country_code(db: Session, country_code: str):
    return db.query(models.Markets).filter\
        (models.Markets.country_code == country_code).all()

def get_markets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Markets).offset(skip).limit(limit).all()

def get_qc_wholesale(db: Session):
    return db.query(models.QC_Wholesale).all()