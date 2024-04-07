from pydantic import BaseModel
from typing import Optional

class FlatData(BaseModel):
    link: str
    name: str
    price: Optional[str] = None
    description: Optional[str] = None
    other_description: Optional[dict] = None
    about_flat: Optional[dict] = None
    about_building: Optional[dict] = None
    goods: Optional[list[str]] = None
    