# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 13:00:58 2017

@author: hyps4
"""
import requests
import time
import pandas as pd
import random
from bs4 import BeautifulSoup

date = pd.read_excel('中国交易所资料/大商所所有品种换约资料/交易日期/IOE1 DATE DATA.xlsx',encoding = 'utf-8')
url = 'http://www.dce.com.cn/publicweb/quotesdata/memberDealPosiQuotes.html'

#以下是分期獲取的代碼
# =============================================================================
# for x in range(0,len(date.dropna())):
#     split_date = date['Date'][x].strftime('%Y-%m-%d').split('-')
#     
#     formData = {'memberDealPosiQuotes.variety':'m',
#             'memberDealPosiQuotes.trade_type':'0',
#             'year':split_date[0],
#             'month':str(int(split_date[1])-1),
#             'day':str(int(split_date[2])),
#             'contract.variety_id':'m'} 
#     res = requests.post(url,data=formData,stream=True)
#     soup = BeautifulSoup(res.text,'lxml')
#     click = (soup.findAll('li',{'class':'keyWord_65'}))
#     res.close()
# =============================================================================
    
for x in range(0,len(date.dropna())): 
    split_date = date['Date'][x].strftime('%Y-%m-%d').split('-')
    
    try:
        data = pd.read_excel('../铁矿石/'+split_date[0]+split_date[1]+split_date[2]+'.xls',encoding='gbk')                  
    except:
        #print (date['Date'][x])
        continue
    data.to_csv('../铁矿石2/'+split_date[0]+split_date[1]+split_date[2]+'.csv',encoding='utf-8-sig',index=None)