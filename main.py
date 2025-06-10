
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from database import SessionLocal, engine
from models import Customer, Gift
from schemas import CustomerCreate, CustomerOut, GiftOut, GiftCreate
import models

# Tạo bảng nếu chưa có
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency để lấy DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/customers/", response_model=CustomerOut)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    db_customer = Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

@app.post("/gifts/", response_model=GiftOut)
def create_gift(gift: GiftCreate, db: Session = Depends(get_db)):
    db_gift = Gift(**gift.dict())
    db.add(db_gift)
    db.commit()
    db.refresh(db_gift)
    return db_gift

@app.get("/customers/{customer_id}", response_model=CustomerOut)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@app.get("/gifts/")
def get_gifts(db: Session = Depends(get_db)):
    gift_list = db.query(Gift).all()
    # gift_list = [
    #     f"{gift.name}, {gift.price}, {gift.description}" for gift in gifts
    # ]
    return gift_list

@app.get("/")
async def redirect_to_docs():
    return RedirectResponse(url="/docs")
