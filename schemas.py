from typing import List, Optional

from pydantic import BaseModel

class Address(BaseModel):
    lat:float
    lng:float