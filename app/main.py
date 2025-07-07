import os

import psycopg2
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "FastAPI is working"}


@app.get("/db")
def test_db():
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    cur = conn.cursor()
    cur.execute("SELECT now()")
    result = cur.fetchone()
    cur.close()
    conn.close()

    return {"db_time": result[0].isoformat()}
