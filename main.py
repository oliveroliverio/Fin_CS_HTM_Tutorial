import sqlite3, configPaper
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def index():
  connection = sqlite3.connect(configPaper.DB_FILE)
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()

  cursor.execute("""
    SELECT id, symbol, name FROM stock
  """)

  rows = cursor.fetchall()

  return {"title": "Dashboard", "stocks": rows}