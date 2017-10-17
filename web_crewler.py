# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 09:58:27 2017

@author: hyps4
"""

import requests
import time
import pandas as pd
import random
from bs4 import BeautifulSoup

date = pd.read_excel('中国交易所资料/大商所所有品种换约资料/交易日期/IOE1 DATE DATA.xlsx',encoding = 'utf-8')
url_excel = 'http://www.dce.com.cn/publicweb/quotesdata/exportMemberDealPosiQuotesData.html'

session = requests.Session()
adapter = requests.adapters.HTTPAdapter(max_retries=20,pool_connections=2)
session.mount('https://', adapter)
session.mount('http://', adapter)

prox = {
        'http':'61.153.67.110:9999',
        'http':'43.240.138.31:8080',
        'http':'121.248.112.20:3128'}
          
for x in range(0,19):
    split_date = date['Date'][x].strftime('%Y-%m-%d').split('-')
    
    formData = {'memberDealPosiQuotes.variety':'i',
                'memberDealPosiQuotes.trade_type':'0',
                'year':split_date[0],
                'month':str(int(split_date[1])-1),
                'day':str(int(split_date[2])),
                'contract.contract_id':'all',
                'contract.variety_id':'i',
                'exportFlag':'excel'}
    tmp = x
        
    res = requests.post(url_excel,data=formData,stream=True)
        
    while(res.status_code != 200):
        res = requests.post(url_excel,data=formData,stream=True)
        time.sleep(random.randrange(2,5))

    with open('../铁矿石/'+split_date[0]+split_date[1]+split_date[2]+'.xls', 'wb') as file:
        file.write(res.content)
    res.close()
    time.sleep(random.randrange(2,5))

