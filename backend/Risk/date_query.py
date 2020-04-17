# function to process user stock query

from datetime import datetime
import numpy as np
import pandas as pd 
import requests
import csv

def stock_query():

    # Need to replace these user inputs with API from frontend
    stock_ticker = input("Stock: ")
    start_date = input("DD/MM/YY: ")
    end_date = input("DD/MM/YY: ")
    direction = input("Up or Down: ")
    price_or_volume = input("Price or Volume: ")           
    datetime_start = datetime.strptime(start_date, '%d/%m/%y')
    datetime_end = datetime.strptime(end_date, '%d/%m/%y')

    # open csv file with filename matching user input
    data_input = stock_ticker
    if not ".csv" in stock_ticker:
        data_input += ".csv"
    df = pd.read_csv(data_input)
    df = df.drop(df.index[0])
    df = df.iloc[:,:-2]
    df['y'] = df[['Open', 'High', 'Low', 'Close']].values.tolist()
    df.drop(['Open', 'High', 'Low', 'Close'], axis=1)
    df['x'] = df['Date']

    # save df as json file to be used for canvasjs chart
    new_df = df[['x', 'y']].copy()  
    file_name = (stock_ticker+"_chart.json")
    new_df.to_json(file_name,orient='index')
    
    # open csv file with filename matching user input
    file_input = stock_ticker
    if not ".csv" in stock_ticker:
        file_input += ".csv"
    stock_df = pd.read_csv(file_input)
    stock_df['Date'] = pd.to_datetime(stock_df['Date']) 
    original_df = stock_df
    mask = (stock_df['Date'] > datetime_start) & (stock_df['Date'] <= datetime_end)
    period_df = stock_df.loc[mask]


    
    # create column for direction up or down
    period_df['Close Minus Open'] = period_df.Close - period_df.Open
    period_df.loc[period_df['Close Minus Open'] >= 0, 'Direction'] = 'Up'
    period_df.loc[period_df['Close Minus Open'] < 0, 'Direction'] = 'Down'

    # get dates that satisfy price change criteria
    if price_or_volume == "Price":
        price_change = input("Price change trigger %: ") 
        price_change = float(price_change)/100
        period_df['Price Change'] = period_df.High / period_df.Low - 1
        period_df.loc[period_df['Price Change'] >= price_change, 'Price Change Date'] = period_df.Date 
        period_df.loc[period_df['Price Change'] < price_change, 'Price Change Date'] = ''
        
        # save dates in json file        
        price_change_dates_df = period_df[['Price Change','Price Change Date','Direction']].copy()
        filter = price_change_dates_df['Price Change Date'] != ""
        price_change_dates_df = price_change_dates_df[filter]
        filter = price_change_dates_df['Direction'] == direction
        price_change_dates_df = price_change_dates_df[filter]
        file_name2 = (stock_ticker+"_price.json")
        price_change_dates_df.to_json(file_name2, orient='index')
        
        # create json file for frontend table
        prices_list = price_change_dates_df.index.tolist()
        week_df = pd.DataFrame(columns = ["Date", "Close"])
        month_df = pd.DataFrame(columns = ["Date", "Close"])
        quarter_df = pd.DataFrame(columns = ["Date", "Close"])
        prices_df = pd.DataFrame(columns = ["Date", "Close"])
        for i in range(0, len(prices_list)): 
            prices_list[i] = int(prices_list[i]) 

            prices_df.loc[len(prices_df)] = original_df.iloc[prices_list[i]]
            week_df.loc[len(week_df)] = original_df.iloc[prices_list[i]]
            month_df.loc[len(month_df)] = original_df.iloc[prices_list[i]]
            quarter_df.loc[len(quarter_df)] = original_df.iloc[prices_list[i]]
            week_df.loc[len(week_df)] = original_df.iloc[prices_list[i]+5]
            month_df.loc[len(month_df)] = original_df.iloc[prices_list[i]+21]
            quarter_df.loc[len(quarter_df)] = original_df.iloc[prices_list[i]+63]
            
            week_df["Week"] = week_df.Close.pct_change(1)
            month_df["Month"] = month_df.Close.pct_change(1)
            quarter_df["Quarter"] = quarter_df.Close.pct_change(1)
        
        week_df_transposed = week_df.T
        month_df_transposed = month_df.T
        quarter_df_transposed = quarter_df.T
        prices_df_transposed = prices_df.T

        #for i in range(0, week_df_transposed.shape[1], 2):
        week_range = range(0, week_df_transposed.shape[1], 2)
        week_df_transposed = week_df_transposed.drop(week_df_transposed.columns[week_range], axis=1)
        month_df_transposed = month_df_transposed.drop(month_df_transposed.columns[week_range], axis=1)
        quarter_df_transposed = quarter_df_transposed.drop(quarter_df_transposed.columns[week_range], axis=1)

        week_df_transposed.drop(['Date','Close'], inplace=True)
        month_df_transposed.drop(['Date','Close'], inplace=True)
        quarter_df_transposed.drop(['Date','Close'], inplace=True)

        week_df_transposed = (week_df_transposed * 100).astype(str) + '%'
        month_df_transposed = (month_df_transposed * 100).astype(str) + '%'
        quarter_df_transposed = (quarter_df_transposed * 100).astype(str) + '%'

        table_df = prices_df_transposed.append(week_df_transposed)
        table_df = table_df.append(month_df_transposed)
        table_df = table_df.append(quarter_df_transposed)

        file_name4 = (stock_ticker+"_table.json")
        table_df.to_json(file_name4)


        
    # get dates that satisfy volume criteria
    elif price_or_volume == "Volume":
        volume_index = input("Volume trigger in millions: ")
        volume_index = float(volume_index)*1000000
        period_df.loc[period_df['Volume'] >= volume_index, 'Volume Index Date'] = period_df.Date 
        period_df.loc[period_df['Volume'] < volume_index, 'Volume Index Date'] = '' 

        # save dates in json file         
        volume_index_dates_df = period_df[['Volume','Volume Index Date','Direction']].copy()
        filter = volume_index_dates_df['Volume Index Date'] != ""
        volume_index_dates_df = volume_index_dates_df[filter]
        filter = volume_index_dates_df['Direction'] == direction
        volume_index_dates_df = volume_index_dates_df[filter]
        file_name3 = (stock_ticker+"_volume.json")
        volume_index_dates_df.to_json(file_name3, orient='index')

        # create json file for frontend table
        prices_list = volume_index_dates_df.index.tolist()
        week_df = pd.DataFrame(columns = ["Date", "Close"])
        month_df = pd.DataFrame(columns = ["Date", "Close"])
        quarter_df = pd.DataFrame(columns = ["Date", "Close"])
        prices_df = pd.DataFrame(columns = ["Date", "Close"])
        for i in range(0, len(prices_list)): 
            prices_list[i] = int(prices_list[i]) 

            prices_df.loc[len(prices_df)] = original_df.iloc[prices_list[i]]
            week_df.loc[len(week_df)] = original_df.iloc[prices_list[i]]
            month_df.loc[len(month_df)] = original_df.iloc[prices_list[i]]
            quarter_df.loc[len(quarter_df)] = original_df.iloc[prices_list[i]]
            week_df.loc[len(week_df)] = original_df.iloc[prices_list[i]+5]
            month_df.loc[len(month_df)] = original_df.iloc[prices_list[i]+21]
            quarter_df.loc[len(quarter_df)] = original_df.iloc[prices_list[i]+63]
            
            week_df["Week"] = week_df.Close.pct_change(1)
            month_df["Month"] = month_df.Close.pct_change(1)
            quarter_df["Quarter"] = quarter_df.Close.pct_change(1)
        
        week_df_transposed = week_df.T
        month_df_transposed = month_df.T
        quarter_df_transposed = quarter_df.T
        prices_df_transposed = prices_df.T

        week_range = range(0, week_df_transposed.shape[1], 2)
        #column_range = range(0, week_df_transposed.shape[1])
        #print(column_range)

        week_df_transposed = week_df_transposed.drop(week_df_transposed.columns[week_range], axis=1)
        month_df_transposed = month_df_transposed.drop(month_df_transposed.columns[week_range], axis=1)
        quarter_df_transposed = quarter_df_transposed.drop(quarter_df_transposed.columns[week_range], axis=1)

        #week_df_transposed.columns = [0,1]
        #month_df_transposed.columns = [0,1]
        #quarter_df_transposed.columns = [0,1]

        week_df_transposed.drop(['Date','Close'], inplace=True)
        month_df_transposed.drop(['Date','Close'], inplace=True)
        quarter_df_transposed.drop(['Date','Close'], inplace=True)

        week_df_transposed = (week_df_transposed * 100).astype(str) + '%'
        month_df_transposed = (month_df_transposed * 100).astype(str) + '%'
        quarter_df_transposed = (quarter_df_transposed * 100).astype(str) + '%'

        table_df = prices_df_transposed.append(week_df_transposed)
        table_df = table_df.append(month_df_transposed)
        table_df = table_df.append(quarter_df_transposed)

        file_name4 = (stock_ticker+"_table.json")
        table_df.to_json(file_name4)
        
stock_query()

    
    


