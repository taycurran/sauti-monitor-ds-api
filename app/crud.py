# allows for declaration of the type of db parameters and 
# better type checks
from sqlalchemy.orm import Session
from . import models, schemas
# ----------------------------------------------------------------------------
def get_market(db: Session, market_name: str):
    return db.query(models.Market).filter\
        (models.Market.market_name == market_name).first()

def get_market_by_country_code(db: Session, country_code: str):
    return db.query(models.Market).filter\
        (models.Market.country_code == country_code).all()

def get_market(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Markets).offset(skip).limit(limit).all()

def get_product_raw_info(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ProductRawInfo).offset(skip).limit(limit).all()