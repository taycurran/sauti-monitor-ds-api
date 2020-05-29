from typing import List
from pydantic import BaseModel

class ProductRawInfoBase(BaseModel):
    product_name: str
    market_id: str
    unit_scale: str
    source_id: int
    currency_code: str
    date_price: str
    retail_observed_price: float
    wholesale_observed_price: float

class ProductRawInfoCreate(ProductRawInfoBase):
    pass

# when reading ProductRawInfo we know the product name and market_id
class ProductRawInfo(ProductRawInfoBase):
    product_name: str
    market_id: str
    # Config class is used to provide configuations to Pydantic
    class Config:
        # this is setting a config value, not declaring a type
        orm_mode = True

# the orm model tells the Pydantic model to read the data even it it
# is not a dict, but an ORM model (or any other arbitrary object with attributes).

class MarketBase(BaseModel):
    market_name: str
    country_code: str

class MarketCreate(MarketBase):
    market_id: str

# when reading markets we declare products will contain the 
# products that belong to a market
class Market(MarketBase):
    id: int
    market_id: str
    market_name: str
    country_code: str
    products: List[ProductRawInfo] = []
    
    class Config:
        orm_mode = True

