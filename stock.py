# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 16:14:38 2021

@author: 85248
"""
import requests

cookies = {
    'xq_a_token': 'a4b3e3e158cfe9745b677915691ecd794b4bf2f9',
    'xqat': 'a4b3e3e158cfe9745b677915691ecd794b4bf2f9',
    'xq_r_token': 'b80d3232bf315f8710d36ad2370bc777b24d5001',
    'xq_id_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTYxNzc2MzQxOCwiY3RtIjoxNjE2MTQ3NDI3NzQ0LCJjaWQiOiJkOWQwbjRBWnVwIn0.Qjvi_Ix8RHTVdUdhirahtjkWKrdBdz3mdtNliBNH0F3mhWNGKNID-LgtvLJoRp88n2YD-gOUFk0WiRvYEVJ2ykt-a0bFGsaOK8G0Ac4mAzBl3XsIxIMI5C_pgqPval6ooFiu5L4Vjjjl7smjIyfnjTaGSm6LNh1utD1rV85prYWvL-rD_jJfU6COTx3S3UUJZ0ee2G4N2J1rCzfG1Cj1lT2N4yMPwaiGv0fwhI-auwAJhQFUUPOtUpRcketg3e6wB0k5sT9-8-9j9F7jBQGLrt2ERkW7RXu4XBkXsSwV-a4FMR3m8MgzxYkXIVv-E58MmFNRUvvohRDpCD3P2EF-lg',
    'u': '291616147471230',
    'Hm_lvt_1db88642e346389874251b5a1eded6e3': '1616147473',
    'Hm_lpvt_1db88642e346389874251b5a1eded6e3': '1616147494',
    'device_id': 'ac9cce0e380c12248598aa0cea7e6744',
    's': 'cd18hbu6vq',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://xueqiu.com/S/SH600396',
    'Origin': 'https://xueqiu.com',
    'Connection': 'keep-alive',
    'TE': 'Trailers',
}

params = (
    ('symbol', 'SH600396'),
    ('begin', '1616234378564'),
    ('period', 'day'),
    ('type', 'before'),
    ('count', '-284'),
    ('indicator', 'kline,pe,pb,ps,pcf,market_capital,agt,ggt,balance'),
)

response = requests.get('https://stock.xueqiu.com/v5/stock/chart/kline.json', headers=headers, params=params, cookies=cookies)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://stock.xueqiu.com/v5/stock/chart/kline.json?symbol=SH600396&begin=1616234378564&period=day&type=before&count=-284&indicator=kline,pe,pb,ps,pcf,market_capital,agt,ggt,balance', headers=headers, cookies=cookies)

# NB. Original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
# response = requests.get('http://66.push2his.eastmoney.com/api/qt/stock/kline/get?cb=jQuery11240360243978561797_1616146959982&secid=0.300059&ut=fa5fd1943c7b386f172d6893dbfba10b&fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5%2Cf6&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2Cf58%2Cf59%2Cf60%2Cf61&klt=101&fqt=0&beg=0&end=20500101&smplmt=460&lmt=1000000&_=1616146960038', headers=headers, cookies=cookies)


# NB. Original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
# response = requests.get('http://huaxiang.eastmoney.com/CommonRecommend.png?json=%7B%22lastModifyTime%22%3A%22_lastModifyTime_%22%2C%22type%22%3A%22pageclick%22%2C%22coord_x%22%3A-11%2C%22coord_y%22%3A712%2C%22elename%22%3A%22DIV%22%2C%22uid%22%3A%22%22%2C%22bid%22%3A%2222330c7d2aadaf0f7b9233d33bcdf727%22%2C%22referer%22%3A%22%22%2C%22pagetype%22%3A%22%22%2C%22pageitem%22%3A%22%22%2C%22browser_height%22%3A424%2C%22from%22%3A%22http%3A%2F%2Fdata.eastmoney.com%2Fzjlx%2Fdetail.html%22%2C%22domainId%22%3A%22data.eastmoney.com%22%2C%22st_pvi%22%3A%2218499695678149%22%2C%22emtj_pageId%22%3A113300300813%7D', headers=headers, cookies=cookies)

## 
print(response)
json_data = response.json()
stock_item = json_data["data"]["item"]
stock_column = json_data["data"]["column"]

import numpy as np
stock_column = np.array(stock_column)
stock_item = np.array(stock_item)
stock_item.reshape((284,24))

import pandas as pd
stock_column = pd.DataFrame(stock_column)
stock_item = pd.DataFrame(stock_item)
stock_data = stock_item
stock_data.columns = stock_column

print(json_data["data"]["symbol"])
print(stock_data)

