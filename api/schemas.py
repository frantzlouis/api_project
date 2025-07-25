from pydantic import BaseModel
from typing import Optional

class CompanySchema(BaseModel):
    name: str
    address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zip: Optional[int]

    class Config:
        orm_mode = True

class ContactSchema(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: str
    phone1: Optional[str]
    phone2: Optional[str]
    department: Optional[str]
    company: Optional[CompanySchema]

    class Config:
        orm_mode = True
