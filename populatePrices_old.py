import configPaper
import alpaca_trade_api as tradeapi

api = tradeapi.REST(configPaper.API_KEY, configPaper.SECRET_KEY, configPaper.API_URL)

# ------for daily bars
# barsets = api.get_barset(['AAPL', 'MFST'], 'day')
# for symbol in barsets:
#   print(f"processing symbol {symbol}")
#   # loop through each bar for the current symbol in dictionary
#   for bar in barsets[symbol]:
#     print(bar.t, bar.o, bar.l, bar.c, bar.v)

# ------for minute bars
minuteBars  = api.polygon.historic_agg_v2('Z', 1, 'minute', _from='2020-10-02', to='2020-10-22')
for bar in minuteBars:
  print(bar.timestamp, bar.open, bar.high, bar.low, bar.close)
