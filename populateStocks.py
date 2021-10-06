import sqlite3, configPaper
import alpaca_trade_api as tradeapi

connection = sqlite3.connect(configPaper.DB_FILE)
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

cursor.execute("""
  SELECT symbol, name FROM stock
""")

rows = cursor.fetchall()
# build list of symbols
symbols = []
for row in rows:
  symbols.append(row['symbol'])

# a shorter way of the above
symbols = [row['symbol'] for row in rows]
# see big 'ol list
# print(symbols)

# create alpaca api client
api = tradeapi.REST(configPaper.API_KEY, configPaper.SECRET_KEY, configPaper.API_URL)
assets =  api.list_assets()

for asset in assets:
  try:
    # check if Alpaca database has new symbols compared to local
    if asset.symbol not in symbols and asset.status == 'active' and asset.tradable:
      print(f"Added a new stock {asset.symbol} {asset.name}")
      cursor.execute("INSERT INTO stock (symbol, name) VALUES (?, ?)", (asset.symbol, asset.name))
  except Exception as e :
    print(asset.symbol)
    print(e)

connection.commit()