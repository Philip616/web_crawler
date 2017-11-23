# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 09:58:27 2017

@author: hyps4
"""

import requests
import time
import pandas as pd
import random
import datetime


url_excel = 'http://www.dce.com.cn/publicweb/quotesdata/exportMemberDealPosiQuotesData.html'

#IP池设定
session = requests.Session()
adapter = requests.adapters.HTTPAdapter(max_retries=20,pool_connections=2)
session.mount('https://', adapter)
session.mount('http://', adapter)

prox = {
        'http':'61.153.67.110:9999',
        'http':'43.240.138.31:8080',
        'http':'121.248.112.20:3128'}
          
now_date = datetime.datetime(2017,11,17)
while now_date < datetime.datetime.now():
    split_date = now_date.strftime('%Y-%m-%d').split('-')
    
    #网站抓取设定
    formData = {'memberDealPosiQuotes.variety':'i',
                'memberDealPosiQuotes.trade_type':'0',
                'year':split_date[0],
                'month':str(int(split_date[1])-1),
                'day':str(int(split_date[2])),
                'contract.contract_id':'all',
                'contract.variety_id':'i',
                'exportFlag':'excel'}
    tmp = now_date
        
    res = requests.post(url_excel,data=formData,stream=True,proxies = prox)
        
    while(res.status_code != 200):
        res = requests.post(url_excel,data=formData,stream=True,proxies = prox)
        time.sleep(random.randrange(2,5))

    #存成excel檔
    with open('../铁矿石/'+split_date[0]+split_date[1]+split_date[2]+'.xls', 'wb') as file:
        file.write(res.content)
    res.close()
    time.sleep(random.randrange(2,5))
    
    #日期加1
    now_date = now_date + datetime.timedelta(days = 1)
    
'''    
#以下是分期獲取的代碼
for x in range(890,len(date.dropna())):
    split_date = date['Date'][x].strftime('%Y-%m-%d').split('-')
    
    formData = {'memberDealPosiQuotes.variety':'i',
            'memberDealPosiQuotes.trade_type':'0',
            'year':split_date[0],
            'month':str(int(split_date[1])-1),
            'day':str(int(split_date[2])),
            'contract.variety_id':'i'} 
    res = requests.post(url,data=formData,stream=True)
    soup = BeautifulSoup(res.text,'lxml')
    click = (soup.findAll('li',{'class':'keyWord_65'}))
    res.close()
    
    tmp = x
    
    for con in click: 
        data = pd.read_excel('./铁矿石_分类/'+split_date[0]+split_date[1]+split_date[2]+'_'+con.get_text(strip=True)+'.xls')                  
        data.to_csv('./铁矿石_分类2/'+split_date[0]+split_date[1]+split_date[2]+'_'+con.get_text(strip=True)+'.csv',encoding='UTF-8-SIG',index=None)
'''