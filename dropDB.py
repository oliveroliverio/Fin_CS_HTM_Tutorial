import sqlite3, configPaper
connection = sqlite3.connect(configPaper.DB_FILE)
cursor = connection.cursor()
cursor.execute("""
  DROP TABLE stock_price
""")
cursor.execute("""

  DROP TABLE stock
""")
connection.commit()