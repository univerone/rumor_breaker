#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Author: Jiang Shanshan
Email: univeroner@gmail.com
Date: 2021/1/23

"""

from typing import Optional

from pydantic import BaseModel


class Rumor(BaseModel):
    id: int = 0
    title: str = None
    LiuyanType: str = None
    answer: str = None
    category: str = None
    date: str = None
    descrip: str = None
    detail: str = None
    pic_url: Optional[str] = None