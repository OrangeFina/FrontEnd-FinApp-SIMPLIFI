#!/usr/bin/env python
# coding: utf-8

# In[30]:


import time
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
import csv
import json
import pandas as pd
import random

#prompt user for input - fixed for now
#user_name = input("What is your name?")
#user_age = input("What is your age?")
#user_job = input("What is your profession?")
#user_study = input("What is your field of study?")
#user_interest = input("What is your interest?")

#READ USER INPUT HERE
user_job = 'Healthcare Professionals - Doctors'
user_study = 'Medicine'
user_interest = 'Fitness'

#OUTPUT BACK INTO THE DICTIONARY

# use panda to read excel
# use userinput profession and education to get sector
with pd.ExcelFile(r'C:\Users\Peng Hong Chua\Documents\yh\FrontEnd-FinApp-SIMPLIFI\backend\Risk\stockexplorer\sectors.xlsx') as xlsx:
    df1 = pd.read_excel(xlsx, 'Professions')
    df2 = pd.read_excel(xlsx, 'Education')
    df3 = pd.read_excel(xlsx, 'Hobbies')

sector_name_1 = df1[df1['Profession'] == str(user_job)]['Relevant Sector']
sector_name_2 = df2[df2['Education'] == str(user_study)]['Relevant Sector']
sector_name_3 = df3[df3['Interests'] == str(user_interest)]['Relevant Sector']

sector_name_1 = list(sector_name_1)
sector_name_2 = list(sector_name_2)
sector_name_3 = list(sector_name_3)

print(sector_name_1)

industries_1 = sector_name_1[0]
industries_2 = sector_name_2[0]
industries_3 = sector_name_3[0]

sector_name_1 = industries_1.split(', ')
sector_name_2 = industries_2.split(', ')
sector_name_3 = industries_3.split(', ')

# choose 3 random sectors from lists and formats it
sector_list = [random.choice(sector_name_1),random.choice(sector_name_2),random.choice(sector_name_3)]
print("Sectors suitable to you are:")
print(sector_list)

#this saves the sector_list to json by turning it into a dataframe first
snap_data = sector_list
snap_headers = ["Sector1","Sector2","Sector3"]
sector_list_json = pd.DataFrame(snap_data,snap_headers)
sector_list_json.to_json(r'C:\Users\Peng Hong Chua\Documents\yh\FrontEnd-FinApp-SIMPLIFI\backend\Risk\stockexplorer\sectorselection.json')
# sector_list_json.to_csv(r'C:\Users\KL\sectorinterest.csv')

#this preps the sector_list for web scrapping
sector_list = [s.replace(' ', '') for s in sector_list]

#this creates a list for the 3 recommended stocks
stock_exp_info = ["company_name_ticker", "profile", "market_cap", "dividend", "shares_outstanding", "shares_float", "prev_close"]
stock_exp = pd.DataFrame(columns=stock_exp_info)

#this creates a list for the individual pages
stock_exp_indiv_info = ("company_name_ticker", "profile", "market_cap", "div", "shares_outstanding", "shares_float", "prev_close", 
                  "fifty_two_weeks", "beta", "net_income", "revenue", "gross_margin", "quick_ratio", "current_ratio",
                  "debt_equity", "op_margin", "profit_margin", "sales_qonq", "roa", "roe", "roi", "eps_ttm", "eps_fwd", "eps_qonq",
                  "book_value_share", "cash_share", "pe", "pe_fwd", "peg", "ps", "pb", "pc", "pfcf")
stock_exp_indiv = pd.DataFrame(columns=stock_exp_indiv_info)

#this generates the json file for the overall stock explorer page
for x in sector_list:
    try:
        #for each industry, run screener to get name + ticker
        url_screen = 'https://finviz.com/screener.ashx?v=111&f=cap_largeover,idx_sp500,ind_' + x +'&o=-marketcap'
        res = requests.get(url_screen)
        soup = BeautifulSoup(res.content, 'html.parser')
        ticker = soup.find_all(class_="screener-link-primary")
        stock = soup.find_all(class_="screener-link")
    
        print(url_screen)
        company_name_ticker = stock[1].get_text() + "(" + ticker[0].get_text() + ")" 
        print(company_name_ticker)

        ticker_name = ticker[0].get_text()

        #for each ticker, go to database and pick out and show Company Profile, MarCap, Div, SharesOut, SharesFloat, PrevClose

        with open('stockdata.json') as json_file:
            data = json.load(json_file)
    
            def get_key(val): 
                for key, value in data['ticker'].items(): 
                     if val == value: 
                        return key 
                return "ERROR"
            
            #this retrieves all relevent info from stock database
            profile = data['profile'][get_key(ticker[0].get_text())]
            market_cap = data['market_cap'][get_key(ticker[0].get_text())]
            dividend = data['dividend'][get_key(ticker[0].get_text())]
            shares_outstanding = data['shares_outstanding'][get_key(ticker[0].get_text())]
            shares_float = data['shares_float'][get_key(ticker[0].get_text())]
            prev_close = data['prev_close'][get_key(ticker[0].get_text())]
                       
            fifty_two_weeks = data['fifty_two_weeks'][get_key(ticker_name)]
            beta = data['beta'][get_key(ticker_name)]
            net_income = data['net_income'][get_key(ticker_name)]
            revenue = data['revenue'][get_key(ticker_name)]
            gross_margin = data['gross_margin'][get_key(ticker_name)]
            quick_ratio = data['quick_ratio'][get_key(ticker_name)]
            current_ratio = data['current_ratio'][get_key(ticker_name)]
            debt_equity = data['debt_equity'][get_key(ticker_name)]
            op_margin = data['op_margin'][get_key(ticker_name)]
            profit_margin = data['profit_margin'][get_key(ticker_name)]
            sales_qonq = data['sales_qonq'][get_key(ticker_name)]
            roa = data['roa'][get_key(ticker_name)]
            roe = data['roe'][get_key(ticker_name)]
            roi = data['roi'][get_key(ticker_name)]
            eps_ttm = data['eps_ttm'][get_key(ticker_name)]           
            eps_fwd = data['eps_fwd'][get_key(ticker_name)]           
            eps_qonq = data['eps_qonq'][get_key(ticker_name)]         
            book_value_share = data['book_value_share'][get_key(ticker_name)]           
            cash_share = data['cash_share'][get_key(ticker_name)]     
            pe = data['pe'][get_key(ticker_name)]
            pe_fwd = data['pe_fwd'][get_key(ticker_name)]
            peg = data['peg'][get_key(ticker_name)]
            ps = data['ps'][get_key(ticker_name)]
            pb = data['pb'][get_key(ticker_name)]
            pc = data['pc'][get_key(ticker_name)]
            pfcf = data['pfcf'][get_key(ticker_name)]
              
            #this appends the overall stock info for the main explorer page
            stock_exp_data = pd.DataFrame([[company_name_ticker, profile, market_cap, dividend, shares_outstanding, shares_float, 
                                            prev_close]],columns=stock_exp_info)
            print(stock_exp_data)
            stock_exp = stock_exp.append(stock_exp_data, ignore_index=True)
            
            #this appends and save stock info for the individual stock page
            stock_indiv = pd.DataFrame([[company_name_ticker, profile, market_cap, dividend, shares_outstanding, shares_float, 
                                         prev_close, fifty_two_weeks, beta, net_income, revenue, gross_margin, quick_ratio, 
                                         current_ratio, debt_equity, op_margin, profit_margin, sales_qonq, roa, roe, roi, eps_ttm, 
                                         eps_fwd, eps_qonq, book_value_share, cash_share, pe, pe_fwd, peg, ps, pb, pc, pfcf]], 
                                        columns=stock_exp_indiv_info)
            
            stock_exp_indiv = stock_exp_indiv.append(stock_indiv, ignore_index=True)
            
            stock_exp_indiv.to_csv(ticker_name +'.csv')
            

            
    # in the event of no stock in sector, it will run generic scrapping of S&P500
    except:
        url_screen = 'https://finviz.com/screener.ashx?v=111&f=cap_largeover,idx_sp500&o=-marketcap'
        res = requests.get(url_screen)
        soup = BeautifulSoup(res.content, 'html.parser')
        ticker = soup.find_all(class_="screener-link-primary")
        stock = soup.find_all(class_="screener-link")
    
        print(url_screen)
        company_name_ticker = stock[1].get_text() + "(" + ticker[0].get_text() + ")" 
        print(company_name_ticker)

        ticker_name = ticker[0].get_text()

        #for each ticker, go to database and pick out and show Company Profile, MarCap, Div, SharesOut, SharesFloat, PrevClose

        with open('stockdata.json') as json_file:
            data = json.load(json_file)
    
            def get_key(val): 
                for key, value in data['ticker'].items(): 
                     if val == value: 
                        return key 
                return "ERROR"
            
                     
            #this retrieves all relevent info from stock database
            profile = data['profile'][get_key(ticker[0].get_text())]
            market_cap = data['market_cap'][get_key(ticker[0].get_text())]
            dividend = data['dividend'][get_key(ticker[0].get_text())]
            shares_outstanding = data['shares_outstanding'][get_key(ticker[0].get_text())]
            shares_float = data['shares_float'][get_key(ticker[0].get_text())]
            prev_close = data['prev_close'][get_key(ticker[0].get_text())]
                       
            fifty_two_weeks = data['fifty_two_weeks'][get_key(ticker_name)]
            beta = data['beta'][get_key(ticker_name)]
            net_income = data['net_income'][get_key(ticker_name)]
            revenue = data['revenue'][get_key(ticker_name)]
            gross_margin = data['gross_margin'][get_key(ticker_name)]
            quick_ratio = data['quick_ratio'][get_key(ticker_name)]
            current_ratio = data['current_ratio'][get_key(ticker_name)]
            debt_equity = data['debt_equity'][get_key(ticker_name)]
            op_margin = data['op_margin'][get_key(ticker_name)]
            profit_margin = data['profit_margin'][get_key(ticker_name)]
            sales_qonq = data['sales_qonq'][get_key(ticker_name)]
            roa = data['roa'][get_key(ticker_name)]
            roe = data['roe'][get_key(ticker_name)]
            roi = data['roi'][get_key(ticker_name)]
            eps_ttm = data['eps_ttm'][get_key(ticker_name)]           
            eps_fwd = data['eps_fwd'][get_key(ticker_name)]           
            eps_qonq = data['eps_qonq'][get_key(ticker_name)]         
            book_value_share = data['book_value_share'][get_key(ticker_name)]           
            cash_share = data['cash_share'][get_key(ticker_name)]     
            pe = data['pe'][get_key(ticker_name)]
            pe_fwd = data['pe_fwd'][get_key(ticker_name)]
            peg = data['peg'][get_key(ticker_name)]
            ps = data['ps'][get_key(ticker_name)]
            pb = data['pb'][get_key(ticker_name)]
            pc = data['pc'][get_key(ticker_name)]
            pfcf = data['pfcf'][get_key(ticker_name)]
              
            #this appends the overall stock info for the main explorer page
            stock_exp_data = pd.DataFrame([[company_name_ticker, profile, market_cap, dividend, shares_outstanding, shares_float, 
                                            prev_close]],columns=stock_exp_info)
            print(stock_exp_data)
            stock_exp = stock_exp.append(stock_exp_data, ignore_index=True)
            
            #this appends and save stock info for the individual stock page
            stock_indiv = pd.DataFrame([[company_name_ticker, profile, market_cap, dividend, shares_outstanding, shares_float, 
                                         prev_close, fifty_two_weeks, beta, net_income, revenue, gross_margin, quick_ratio, 
                                         current_ratio, debt_equity, op_margin, profit_margin, sales_qonq, roa, roe, roi, eps_ttm, 
                                         eps_fwd, eps_qonq, book_value_share, cash_share, pe, pe_fwd, peg, ps, pb, pc, pfcf]], 
                                        columns=stock_exp_indiv_info)
            
            stock_exp_indiv = stock_exp_indiv.append(stock_indiv, ignore_index=True)
            
            stock_exp_indiv.to_csv(ticker_name +'.csv')
            
    
stock_exp.to_json(r'C:\Users\Peng Hong Chua\Documents\yh\FrontEnd-FinApp-SIMPLIFI\backend\Risk\stockexplorer\stockexplorermain.json')
# stock_exp.to_csv(r'C:\Users\KL\stockexplorermain.csv')

