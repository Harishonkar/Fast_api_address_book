from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

# Create a sqlite engine instance
engine = create_engine("sqlite:///todooo.db")

# Create a DeclarativeMeta instance
Base = declarative_base()

# Define To Do class inheriting from Base
class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    lat =  Column(Float)
    lng = Column(Float)
# Create the database
Base.metadata.create_all(engine)