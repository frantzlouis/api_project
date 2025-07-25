from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, crud
from schemas import ContactSchema

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/contacts/", response_model=list[ContactSchema])
def read_contacts(db: Session = Depends(get_db)):
    return crud.get_all_contacts(db)
