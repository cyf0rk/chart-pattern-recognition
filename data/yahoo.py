import yfinance as yf

slack = yf.Ticker("AAPL")

history = slack.history(period="max")

history.to_csv()
