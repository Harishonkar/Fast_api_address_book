from typing import Optional
from fastapi import FastAPI
from schemas import Address
from sqlalchemy.orm import Session
from database import Base, engine
from database import Address as AddressTable, SessionLocal

from query import get_address as get_address_loc, update_address_loc, delete_address_loc, get_addresses_in_radoius


app = FastAPI()

# Create the database
Base.metadata.create_all(engine)



@app.get("/address/")
def get_addresses():

    # create a new database session
    session = Session(bind=engine, expire_on_commit=False)
   
    addresses = get_address_loc(session)
    session.close()
    return {"addresses": addresses}

@app.post("/address/")
def create_address(address:Address):
    # create a new database session
    session = Session(bind=engine, expire_on_commit=False)

    # create an instance of the ToDo database model
    address_obj = AddressTable(lat = address.lat, lng=address.lng)

    # add it to the session and commit it
    session.add(address_obj)
    session.commit()

    # grab the id given to the object from the database
    id = address_obj.id

    # close the session
    session.close()

    # return the id
    return f"created todo item with id {id}"


@app.get("/address/{id}")
def get_address_by_id(id):
    session = Session(bind=engine, expire_on_commit=False)
    addresses = get_address_loc(session, id)
    session.close()
    return {"addresses": addresses}



@app.put("/address/{id}")
def update_address(id, address:Address):
    session = Session(bind=engine, expire_on_commit=False)
    res=update_address_loc(session, id, address)
    session.close()
    return res


@app.delete("/address/{id}")
def delete_address(id, address:Address):
    session = Session(bind=engine, expire_on_commit=False)
    res=delete_address_loc(session, id)
    session.close()
    return res

@app.get("/address/get_address_in_radius/")
def get_address_in_radoius(radius, lat, lng):
    session = Session(bind=engine, expire_on_commit=False)
    res=get_addresses_in_radoius(session, radius, lat, lng)
    session.close()
    return res
