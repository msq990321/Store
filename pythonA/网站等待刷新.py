# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 20:15:54 2022

@author: Administrator
"""


import requests
import time

urls = ['http://httpstat.us/500']

def get_data(url,num_retries = 3):
    try:
        data = requests.get(url,timeout = 5)
        print(data.status_code)
    except requests.exceptions.ConnectionError as e:
        print('请求错误,url:',url)
        print('错误详情',e)
        data = None
    except:
        print('未知错误,url:',url)
        data = None
    
    if (data !=None) and (500<= data.status_code<600):
        if(num_retries>0):
            print('服务器错误，正在重试...')
            time.sleep(1)
            num_retries -= 1
            get_data(url,num_retries)
    return data
            
            
if __name__ == '__main__':
    for url in urls:
        get_data(url)