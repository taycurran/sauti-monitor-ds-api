from typing import List
from pydantic import BaseModel

# the orm model tells the Pydantic model to read the data even it it
# is not a dict, but an ORM model (or any other arbitrary object with attributes).

class MarketBase(BaseModel):
    id: int
    market_name: str
    country_code: str
    market_id: str


class Market(MarketBase):
    id: int
    market_id: str
    market_name: str
    country_code: str
    
    class Config:
        orm_mode = True

class QCWholesaleBase(BaseModel):
    market_name: str
    product: str
    source: str
    start: str
    end: str
    timeliness: str
    data_length: str
    completeness: str
    duplicates: str
    mode_D: str

class QCWholesale(QCWholesaleBase):
    market_name: str
    product: str
    source: str
    start: str
    end: str
    timeliness: str
    data_length: str
    completeness: str
    duplicates: str
    mode_D: str

    class Config:
        orm_mode = True

