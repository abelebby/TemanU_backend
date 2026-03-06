from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()

@app.post("/register")
def register(user: schemas.UserCreate, database: Session = Depends(get_db)):

    new_user = models.User(
        email=user.email,
        name=user.name,
        preferred_name=user.preferred_name,
        username=user.username,
        password_hash=user.password_hash
    )

    database.add(new_user)
    database.commit()
    database.refresh(new_user)

    return {"message": "User created successfully", "id": new_user.id}