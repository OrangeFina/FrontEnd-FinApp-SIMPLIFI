from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Risk
from .serializers import RiskSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView


import time
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
import csv
import json
import pandas as pd

from random import *
import statistics
import shutil
import os
import datetime
import numpy as np
import random



# Create your views here.
@csrf_exempt
def risk_list(request):
        # instantiates the QueryDict from request.GET
        # create a list of user inputs   
    content = request.GET
    user_answer = content.getlist('question')
    print("user_answer: ",user_answer)    
    #assume response given is questionnaire(11 responses) followed by counter
    sample_input = "a,a,a,a,a,a,a,a,a,a,a,business,chemist,basketball,50"

    # button game data
    counter_raw_data = [69, 92, 48, 47, 120, 60, 100, 88, 88, 100, 55, 30, 35, 90, 99, 120, 30, 69, 88, 101, 95, 90, 66, 67,
                        67, 43, 108, 150, 100, 70]



    #=================== JSON STUFF ======================#
    # forms a random integer of a user
    # check if it already exists in the dictionary (username is key in dict)
    # if it does get another number
    # else add dictionary into file

    #ISSUES: cant get the entering professions to work yet since it enters every key (unless theres autocomplete)

    x = randint(1,100)
    username = "user" + str(x)
    password = username
    userkey = username
    data = {}
        # with open('maindb.txt','w') as f:
        #     data = json.load(f)

    while userkey in data:
        x = randint(1,100)
        username = "user" + str(x)
        password = username
        userkey = username

    print("generated user: ",username)

    username = {
        "username" : username,
        "password" : password,
        "answers" : user_answer[0:11],
        "education" : user_answer[11],
        "profession" : user_answer[12],
        "interest" : user_answer[13]
    }

    data[userkey] = username

    # loads dictionary and adds it before dumping it in
    with open('maindb.txt', 'r') as f:
        contents = str(f.read())
        contents = contents.replace("\\","")
        contents = json.loads(contents)
        print("raw: ",contents)
        finalList = []
        for item in contents:
            finalList.append(item)
        finalList.append(data)
        print("final: ",finalList)
        rawList = json.dumps(finalList)

    with open('maindb.txt','w') as g:
        g.write(rawList)
    
    # shutil.move("maindb.txt","")
    return HttpResponse("success")

#================ OLD MARKING SCHEME ==================#


    # # instantiates the QueryDict from request.GET
    # # create a list of user inputs
    
    # content = request.GET
    # user_answer = content.getlist('question')
    # print(user_answer)


    # # context_data = {'question': user_answer}
    # # if user_answer is None:
    # #     return JsonResponse(data=context_data)
    
    # # assume response given is questionnaire(11 responses) followed by counter
    # # sample input = "a,a,a,a,a,a,a,a,a,a,a,50"
    # # response = "a,a,a,a,a,a,a,a,a,a,a,50"

    # #button game data
    # counter_raw_data = [69, 92, 48, 47, 120, 60, 100, 88, 88, 100, 55, 30, 35, 90, 99, 120, 30, 69, 88, 101, 95, 90, 66, 67, 67, 43, 108, 150, 100, 70]


    # #iterates the list to convert all char to upper
    # full_input = map(str.upper,user_answer)

    # print(full_input)
    # limit = 0
    # user_input = []
    # for inputs in full_input:
    #     user_input.append(inputs)
    #     limit += 1
    #     if limit == 11:
    #         break

    # counter_input = 0
    # count_limit = 0
    # for inputs in full_input:
    #     count_limit += 1
    #     if count_limit > 11:
    #         counter_input = int(inputs)

    # score = 0
    # user_profile = ""

    # for response in user_input:
    #     if response == "A":
    #         score += 1
    #     elif response == "B":
    #         score += 3
    #     elif response == "C":
    #         score += 5


    #=========================== BUTTON GAME CALCULATIONS ===========================

    # sd = statistics.stdev(counter_raw_data) * 2
    # mean = statistics.mean(counter_raw_data)
    # intermediate = int(mean-sd)    

    # if counter_input <= intermediate:
    #     score += 15
    # elif counter_input > mean - sd and counter_input <= mean:
    #     deviate = int((abs(counter_input - mean) / sd * 6))
    #     score += 9 + deviate
    # elif counter_input > mean and counter_input <= mean + sd:
    #     deviate = int((abs(counter_input - mean) / sd * 6))
    #     score += 9 - deviate
    # elif counter_input > mean + sd:
    #     score += 3
    
    # if score <= 21:
    #     user_profile = "Aggressive"


    # elif score > 21 and score <= 34:
    #     user_profile = "Moderate Balance"


    # elif score > 35 and score <= 47:
    #     user_profile = "Growth Balance"


    # elif score > 48:
    #     user_profile = "Conservative"

    # print("score before button game: " + str(score))
    # context = {
    #     'score' : score
    #     # 'userprofile': user_profile
    # }

    # return JsonResponse("score = " + str(score), safe=False)

def questionnaire(request):
    content = request.GET
    user_answer = content.getlist('count')
    print("user_count: ",user_answer)   
    combined_profiles = []
    user_profile = ""

    #need to retrieve this from frontend

    # need to get the username thing

    dbList = []
    print("Started Reading JSON file which contains multiple JSON document")
    with open("maindb.txt","r") as f:
        dbList = str(f.read())
        dbList = json.loads(dbList)

    # for line in open('maindb.txt', 'r+'):
    #     dbList.append(json.loads(line))
    # print (dbList)
    dbList = dict((key, val) for k in dbList for key, val in k.items())
    print(dbList)
    place = list(dbList.keys())[-1]
    user_dict = dbList[place]
    user_input = user_dict["answers"]

    # iterates the list to convert all char to upper
    full_input = map(str.upper, user_input)
    limit = 0
    user_input = []
    for inputs in full_input:
        user_input.append(inputs)
        limit += 1
        if limit == 11:
            break
    print("user input: ",user_input)
    # determine who is the user
    # link it to the "answers" in the dictionary
    
    # =========================== Willingness ===========================
    willingness = [0,3,5,7,8,9]
    willingness_input = []
    willingness_score = 0

    #filter out willingness questions
    for x in willingness:
        willingness_input.append(user_input[x])

    print("Willingness: ",willingness_input)

    #calculate willingness score
    for response in willingness_input:
        if response == "A":
            willingness_score += 1
        elif response == "B":
            willingness_score += 3
        elif response == "C":
            willingness_score += 5
    print("willingness score: ",willingness_score)

    #match willingness score to profile
    if willingness_score <= 8:
        combined_profiles.append(4)

    elif willingness_score >= 9 and willingness_score <= 16:
        combined_profiles.append(3)

    elif willingness_score >= 17 and willingness_score <= 25:
        combined_profiles.append(2)

    elif willingness_score >= 26:
        combined_profiles.append(1)

    # print(combined_profiles)


    # =========================== Ability ===========================
    ability = [1,2,4,10]
    ability_input = []
    ability_score = 0

    for x in ability:
        ability_input.append(user_input[x])

    print("Ability: ", ability_input)

    #calculate ability score
    for response in ability_input:
        if response == "A":
            ability_score += 1
        elif response == "B":
            ability_score += 3
        elif response == "C":
            ability_score += 5
    print("ability score: " ,ability_score)


    #match ability score to profile
    if ability_score <= 6:
        combined_profiles.append(4)

    elif ability_score >= 7 and ability_score <= 11:
        combined_profiles.append(3)

    elif ability_score >= 12 and ability_score <= 16:
        combined_profiles.append(2)

    elif ability_score >= 17:
        combined_profiles.append(1)


    # =========================== BUTTON GAME CALCULATIONS ===========================#
    # button game data
    counter_raw_data = [69, 92, 48, 47, 120, 60, 100, 88, 88, 100, 55, 30, 35, 90, 99, 120, 30, 69, 88, 101, 95, 90, 66, 67,
                        67, 43, 108, 150, 100, 70]
    sd = statistics.stdev(counter_raw_data) * 2
    mean = statistics.mean(counter_raw_data)
    intermediate = int(mean-sd)
    counter_input = int(user_answer[0])

    if counter_input <= intermediate:
        combined_profiles.append(4)

    elif counter_input > mean - sd and counter_input <= mean:
        combined_profiles.append(3)

    elif counter_input > mean and counter_input <= mean + sd:
        combined_profiles.append(2)

    elif counter_input > mean + sd:
        combined_profiles.append(1)

    
    combined_profiles.sort(reverse=True)
    print(combined_profiles[0])

    if combined_profiles[0] == 1:
        user_profile = "Aggressive"


    elif combined_profiles[0] == 2:
        user_profile = "Growth Balance"


    elif combined_profiles[0] == 3:
        user_profile = "Moderate Balance"


    elif combined_profiles[0] == 4:
        user_profile = "Conservative"

    print("User is : ",user_profile)

    # adds the user profile into the database
    user_dict["user_profile"] = user_profile
    print(user_dict)
    dbList[place]["counter_game"] = user_answer
    dbList[place]["user_profile"] = user_profile
    print("final dict: ",dbList)
    # writes it back

    with open('maindb.txt','w') as g:
        # qContents = json.loads(dbList)
        
        qList = json.dumps([dbList])
        g.write(str(qList))
    
    copyfile("maindb.txt")
    stockexplorer(place)

    return HttpResponse("success")


def database(request):
    print(os.getcwd())
    f = open('maindb.txt', 'r+')
    file_content = f.read()
    # file_content = json.loads(file_content)
    copyfile("maindb.txt")
    return HttpResponse(file_content, content_type="text/plain")


def allocation(request):
    f = open('maindb.txt', 'r+')
    file_content = f.read()
    # file_content = json.loads(file_content)
    json_data = {"state": 2}
    return render(request,"frontend/src/components/allocation.jsx",json.dump(file_content))


def stockexplorer(userid):
    #!/usr/bin/env python
    # coding: utf-8
    #prompt user for input - fixed for now
    #user_name = input("What is your name?")
    #user_age = input("What is your age?")
    #user_job = input("What is your profession?")
    #user_study = input("What is your field of study?")
    #user_interest = input("What is your interest?")
    dbList = []
    print("Started Reading JSON file which contains multiple JSON document")
    with open("maindb.txt","r") as f:
        dbList = str(f.read())
        dbList = json.loads(dbList)
    dbList = dict((key, val) for k in dbList for key, val in k.items())
    # place = list(dbList.keys())[-1]
    user_dict = dbList[userid]
    user_job = user_dict["profession"]
    user_study = user_dict["education"]
    user_interest = user_dict["interest"]

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

    print("user job: ",user_job)
    print(sector_name_1)
    print(sector_name_2)
    print(sector_name_3)

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
    sector_list = [s.replace('&', '') for s in sector_list]

    #this creates a list for the 3 recommended stocks
    stock_exp_info = ["company_name_ticker", "profile", "market_cap", "dividend", "shares_outstanding", "shares_float", "prev_close"]
    stock_exp = pd.DataFrame(columns=stock_exp_info)

    #this creates a list for the individual pages
    stock_exp_indiv_info = ("company_name_ticker", "profile", "market_cap", "div", "shares_outstanding", "shares_float", "prev_close", 
                    "fifty_two_weeks", "beta", "net_income", "revenue", "gross_margin", "quick_ratio", "current_ratio",
                    "debt_equity", "op_margin", "profit_margin", "sales_qonq", "roa", "roe", "roi", "eps_ttm", "eps_fwd", "eps_qonq",
                    "book_value_share", "cash_share", "pe", "pe_fwd", "peg", "ps", "pb", "pc", "pfcf")
    stock_exp_indiv = pd.DataFrame(columns=stock_exp_indiv_info)
    name_counter = 0
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
                
                stock_exp_indiv.to_csv(str(name_counter) +'.csv')
                stock_indiv.to_json(str(name_counter)+'.json')
                finalPath = r'C:\Users\Peng Hong Chua\Documents\yh\FrontEnd-FinApp-SIMPLIFI\frontend\src\components'
                copyfile(str(name_counter)+'.json')
                name_counter += 1
                

                
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
                
                stock_exp_indiv.to_csv(str(name_counter) +'.csv')
                stock_indiv.to_json(str(name_counter)+'.json')
                finalPath = r'C:\Users\Peng Hong Chua\Documents\yh\FrontEnd-FinApp-SIMPLIFI\frontend\src\components'
                copyfile(str(counter)+'.json')
                name_counter=  name_counter+1
                
        
    stock_filename =  r'C:\Users\Peng Hong Chua\Documents\yh\FrontEnd-FinApp-SIMPLIFI\backend\Risk\stockresult.json'
    stock_exp.to_json(stock_filename)
    # stock_exp.to_csv(r'C:\Users\KL\stockexplorermain.csv')
    copyfile(stock_filename)
    convertJson("maindb.txt")
    copyfile("maindb.json")
        

def copyfile(filename):
    #up 1 level to risk
    print(os.getcwd())
    path = os.path.dirname(os.getcwd())
    #up 1 level to backend
    #up 1 level to root folder
    path = os.path.dirname(path)
    #navigate to components folder
    path = os.path.dirname(r"C:\Users\Peng Hong Chua\Documents\yh\FrontEnd-FinApp-SIMPLIFI\frontend\src\components\maindb.txt")
    print(path)

    shutil.copy2(filename,path)


def stock_query(request):
    content = request.GET
    user_answer = content.getlist('question')
    print("user_answer: ",user_answer)
    # Need to replace these user inputs with API from frontend
    stock_ticker = user_answer[0]
    start_date = user_answer[1]
    end_date = user_answer[2]
    
    if user_answer[3] == "Pos":
        direction = "Up"
    else:
        direction = "Down"
    sortnews(stock_ticker,start_date,end_date,direction)
    price_or_volume = "Price"         
    datetime_start = datetime.datetime.strptime(start_date, '%d/%m/%y')
    datetime_end = datetime.datetime.strptime(end_date, '%d/%m/%y')

    # open csv file with filename matching user input
    os.chdir(r'C:\Users\Peng Hong Chua\Documents\yh\FrontEnd-FinApp-SIMPLIFI\backend\Risk\graph_tickers')
    
    data_input = stock_ticker
    if not ".csv" in stock_ticker:
        data_input += ".csv"
    df = pd.read_csv(data_input)
    df = df.drop(df.index[0])
    df = df.iloc[:,:-2]
    df['y'] = df[['Open', 'High', 'Low', 'Close']].values.tolist()
    df.drop(['Open', 'High', 'Low', 'Close'], axis=1)
    df['Date'] = pd.to_datetime(df['Date'])
    df['x'] = df['Date']

    # save df as json file to be used for canvasjs chart
    new_df = df[['x', 'y']].copy()  
    file_name = ("ticker_chart.json")
    dateLimit = (new_df['x'] > datetime_start) & (new_df['x'] <= datetime_end)
    saved_df = new_df.loc[dateLimit]
    saved_df.to_json(file_name,orient='index')
    reformatJson()
    copygraphfile(file_name)
    
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
        price_change = 3
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
        file_name2 = ("ticker_price.json")
        price_change_dates_df.to_json(file_name2, orient='index')
        copygraphfile(file_name2)
        
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

        file_name4 = ("ticker_table.json")
        table_df.to_json(file_name4)
        print(table_df)
        copygraphfile(file_name4)


        
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
        copygraphfile(filename4+'.json')
        
    return HttpResponse("Success")

def copygraphfile(filename):

    print(os.getcwd())
    #up 1 level to risk
    path = os.path.dirname(os.getcwd())
    #up 1 level to backend
    path = os.path.dirname(path)
    #up 1 level to root folder
    path = os.path.dirname(path)
    #navigate to components folder
    path = os.path.dirname(path+r"\frontend\src\components\"")
    print(path)

    shutil.copy2(filename,path)
    
    path = r"C:\Users\Peng Hong Chua\Documents\yh\FrontEnd-FinApp-SIMPLIFI\backend\Risk\risk_api"
    shutil.copy2(filename,path)
    
    
def chartdatabase(request):
    print(os.getcwd())
    
    f = open(r'C:\Users\Peng Hong Chua\Documents\yh\FrontEnd-FinApp-SIMPLIFI\backend\Risk\risk_api\ticker_chart.json', 'r')
    file_content = f.read()
    # file_content = json.loads(file_content)
    # copyfile("maindb.txt")
    return HttpResponse(file_content, content_type="text/plain")


def convertJson(filename):
    
    
    thisFile = filename
    base = os.path.splitext(thisFile)[0]
    # os.rename(thisFile, base + ".json")
    shutil.copy2("maindb.txt","maindb.json")  
    
    
def reformatJson():
    myFile = "ticker_chart.json"
    with open(myFile, 'r+') as f:
        contents = str(f.read())
        contents = contents.replace("\\","")
        contents = json.loads(contents)
        # print("raw: ",contents)
        finalList = []
        for item in contents:
            finalList.append(item)
        # print("final: ",finalList)
        # print("rawlist: ",rawList)
        
        dictlist = []
        for key, value in contents.items():
            temp = value
            dictlist.append(temp)
        # print(dictlist)
        rawList = json.dumps(dictlist)
    
    with open('ticker_chart.json','w') as g:
        g.write(rawList)
  
    

def sortnews(counter,start_date,end_date,direction):
    ticker= counter
    datetime_start = datetime.datetime.strptime(start_date, '%d/%m/%y')
    datetime_end = datetime.datetime.strptime(end_date, '%d/%m/%y')
    delta = datetime.timedelta(days=1)
    df = pd.read_json(r'C:\Users\Peng Hong Chua\Documents\yh\FrontEnd-FinApp-SIMPLIFI\backend\Risk\risk_api\news.json')
    condition1 = df['Counter'] == counter
    condition3 = df['Direction'] == direction 


    c_df = df.loc[df['Counter'] == ticker]
    cd_df = c_df.loc[c_df['Direction'] == direction]
    # cd_df['Date'] = pd.to_datetime(cd_df['Date'], format ="%d/%d/%y")
    
    # print(cd_df)
    df1 = pd.DataFrame()
    
    while datetime_start <= datetime_end:
        time_df = cd_df.loc[cd_df['Date'] == datetime_start.strftime("%Y-%m-%d")]
        # print(time_df)
        df1 = df1.append(time_df, ignore_index = True)
        datetime_start += delta
        # print(datetime_start.strftime("%x"))
    # print(df1)
    df1 = df1.reset_index()
    df1.to_json("collatednews.json")
    copyfile("collatednews.json")
            
            
    #     condition1 = df['Counter'] == counter
    #     print(condition1) 
    #     condition2 = df['Date'] == str(datetime_start)
    #     print(condition2)
    #     condition3 = df['Direction'] == direction
    #     print(condition3) 
    #     if df[condition1 & condition2 & condition3].empty:
    #         x += 1
    #     else:
    #         print(df[condition1 & condition2 & condition3])
    #     datetime_start += delta
    # df = df[condition1 & condition2]
    # df.to_json("conditionNews.json")


