
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
from datetime import datetime
import numpy as np
import random


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


    