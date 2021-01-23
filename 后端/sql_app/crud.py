#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Author: Jiang Shanshan
Email: univeroner@gmail.com
Date: 2021/1/23

"""

from sqlalchemy.orm import Session

import models


def search_rumor(db: Session, title_contains: str, skip: int = 0, limit: int = 100):
    return db.query(models.Rumor)\
        .order_by(models.Rumor.date.desc())\
        .filter(models.Rumor.title.contains(title_contains))\
        .offset(skip)\
        .limit(limit)\
        .all()

def get_rumor(db: Session, id: int):
    return db.query(models.Rumor).filter(models.Rumor.id == id).first()

def get_rumor_by_category(db: Session, category: str, skip: int = 0, limit: int = 100):
    return db.query(models.Rumor).order_by(models.Rumor.date.desc()).filter(models.Rumor.category == category).offset(skip).limit(limit).all()