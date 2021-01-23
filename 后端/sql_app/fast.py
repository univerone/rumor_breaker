#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Author: Jiang Shanshan
Email: univeroner@gmail.com
Date: 2021/1/23

"""
from typing import List

import uvicorn
import fastapi_csv
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8080/h5/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "Hello World"}

@app.get("/rumors/category/")
def get_rumor_by_category(category, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_rumor_by_category(db, category=category, skip=skip, limit=limit)
    return users

@app.get("/rumors/{id}")
def get_rumor(id: int, db: Session = Depends(get_db)):
    db_user: schemas.Rumor = crud.get_rumor(db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/rumors/search/")
def search_rumor(title_contains, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.search_rumor(db, title_contains=title_contains, skip=skip, limit=limit)
    return users

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)