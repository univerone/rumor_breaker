#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Author: Jiang Shanshan
Email: univeroner@gmail.com
Date: 2021/1/23

"""
from sqlalchemy import Column, Integer, String

from database import Base


class Rumor(Base):
    """
    id:编号
    title: 流言标题（字数尽量少）
    descrip: 流言详细内容（看字数决定用不用）
    LiuyanTyp: 留言类别（真、假）
    detail:
    answer: 详细解析（网页中的论证内容，包括html样式）
    date:
    pic_url:
    """
    __tablename__ = "rumor"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    LiuyanType = Column(String)
    answer = Column(String)
    category = Column(String)
    date = Column(String)
    descrip = Column(String)
    detail = Column(String)
    pic_url = Column(String)