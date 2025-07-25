from sqlalchemy.orm import Session
from models import Contact

def get_all_contacts(db: Session):
    return db.query(Contact).join(Contact.company).all()
