# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 09:58:27 2017

@author: hyps4
"""

import requests
import time
import pandas as pd
import random

date = pd.read_excel('副本鐵礦石交易日期.xlsx')
url_excel = 'http://www.dce.com.cn/publicweb/quotesdata/exportMemberDealPosiQuotesData.html'
count = 0
for x in range(140,1013):
    split_date = date['Date'][x].strftime('%Y-%m-%d').split('-')
    
    formData = {'memberDealPosiQuotes.variety':'i',
                'memberDealPosiQuotes.trade_type':'0',
                'year':split_date[0],
                'month':str(int(split_date[1])-1),
                'day':str(int(split_date[2])),
                'contract.contract_id':'all',
                'contract.variety_id':'i',
                'exportFlag':'excel'}   
    
    res = requests.post(url_excel,data=formData,stream=True)
    with open('./铁矿石/'+split_date[0]+split_date[1]+split_date[2]+'_铁矿石.xls', 'wb') as file:
        file.write(res.content)
    res.close()
    time.sleep(random.randrange(1,3))