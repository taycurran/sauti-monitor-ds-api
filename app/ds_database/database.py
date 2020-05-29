from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
load_dotenv()

# Create Connection Engine
# represents the core interface to the database
engine = create_engine(os.getenv("aws_db_url"), echo=True)

# Define Class
#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# returns a class
Base = declarative_base()