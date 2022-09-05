# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 16:03:49 2022

@author: Administrator
"""


import requests
urls = ['http://www.baidussss.com','http://news.baidu.com','http://datahonor.com/404','http://httpstat.us/500']


def get_data(url):
    try:
        data = requests.get(url)
    except requests.exceptions.ConnectionError as e:
        print('请求错误,url：',url)
        print('错误详情：',e)
        data = None
    return data

if __name__ == '__main__':
    for url in urls:
        get_data(url)