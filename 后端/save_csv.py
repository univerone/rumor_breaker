#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Author: Jiang Shanshan
Email: univeroner@gmail.com
Date: 2021/1/23

"""
import json
import logging
import sqlite3
from pathlib import Path

import pandas as pd
import numpy as np


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def main():
    logging.info("Creating new database...")
    df1 = pd.read_csv('/home/shanshan/github/挑战杯项目/rumor_breaker/后端/liuyan.csv', keep_default_na=False)
    df2 = pd.read_csv('/home/shanshan/github/挑战杯项目/rumor_breaker/后端/Guok.csv', keep_default_na=False)
    df1 = df1[['LiuyanType','answer','category','date','descrip','detail','title', 'pic_url' ]]
    df2 = df2[['LiuyanType','answer','category','date','descrip','detail','title']]
    df2['pic_url'] = np.zeros(len(df2))
    df3 = df1.append(df2)
    df3['id'] = np.arange(df3.shape[0])
    con = sqlite3.connect("database.db", check_same_thread=False)
    df3.to_sql('rumor', con)
    con.row_factory = dict_factory

def json_to_csv(json_file_name: str):
    with open(json_file_name) as json_file:
        data = json.load(json_file)
    return data

if __name__ == '__main__':
    main()
