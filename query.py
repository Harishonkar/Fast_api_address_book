from sqlalchemy.orm import Session
import  database
from get_distance import calculate_deo_distance


def get_address(db: Session, id:int=None):
    if id:
        return db.query(database.Address).filter(database.Address.id == id).first()
    else:
        return db.query(database.Address).all()

def update_address_loc(db: Session, id:int, address:database.Address):
    address_obj = db.query(database.Address).get(id)
    if address_obj:
        address_obj.lat= address.lat
        address_obj.lng= address.lng
        db.commit()
        return {"status":"success"}

    else:
        return {"status":"failed", "msg":"entry with given id not found"}

def delete_address_loc(db: Session, id:int):
    address_obj = db.query(database.Address).get(id)
    if address_obj:
        db.delete(address_obj)
        db.commit()
        return {"status":"success"}

    else:
        return {"status":"failed", "msg":"failed to delete object"}

def get_addresses_in_radoius(db: Session, radius:int, lat: float, lng: float):
    address_objs = db.query(database.Address).all()
    stores=[addr for addr in address_objs if calculate_deo_distance((float(lat),float(lng)),(float(addr.lat), float(addr.lng)), radius)]
    return stores