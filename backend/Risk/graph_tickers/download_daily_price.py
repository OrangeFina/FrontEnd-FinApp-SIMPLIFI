# function to pull daily price and save each file as csv
def pull_stock_data():
    import bs4 as bs
    import requests
    import datetime
    import yfinance as yf
    import pandas as pd
    import numpy as np

# extracting current list of all stocks in S&P 500 from wikipedia
    resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)

# downloading stock data from yahoo finance for all stocks which are in S&P500 for max history
    tickers = [s.replace('\n', '') for s in tickers]
    #start = datetime.datetime(2019,1,1)
    #end = datetime.datetime(2019,12,31)

# create dictionary for stocks and dataframes
    stocks_dict = {}
    stocks_df = {}

# download individual data for each stock and create individual dataframe
    for i in tickers:
        stocks_dict["{0}".format(i)] = yf.download(i, period="max")
        stocks_df["{0}".format(i)] = pd.DataFrame(stocks_dict[i])
    
    #stocks_df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']

# save each dataframe as json
    for index, df in stocks_df.items():
        file_name=(index+".csv")
        df.to_csv(file_name)

# to call function
pull_stock_data()
