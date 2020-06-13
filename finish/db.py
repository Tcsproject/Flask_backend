from sqlalchemy import Column, Integer, DateTime
import sqlite3
import os
import pandas as pd
BASE_DIR = os.path.dirname(os.getcwd())
db_path = os.path.join(BASE_DIR, "finish\database.db")
print(db_path)
con = sqlite3.connect(db_path)
cur = con.cursor()
df_match = pd.read_sql_query("SELECT * from user;", con)
print(df_match['username'])
