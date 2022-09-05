# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 14:33:26 2022

@author: Administrator
"""


import re
import requests
import time
from fake_useragent import UserAgent
import chardet
import urllib.robotparser

#获取headers
def get_headers():
    ua = UserAgent()
    user_agent = ua.random
    headers = {'User-Agent':user_agent}
    return headers


#代理IP
def get_proxies():
    proxies = {
        'http':'125.88.74.122:84',
        'http':'123.84.13.240:8118',
        'http':'94.240.33.242:3128'}
    return proxies

#robots.txt检测
def robot_check(robotstxt_url,headers,url):
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(robotstxt_url)
    rp.read()
    result = rp.can_fetch(headers['User-Agent'], url)
    return result

#获取网页数据，这里没有返回data.text，
#因为抓取图片时应该是data.content
def get_data(url,num_retries = 3,proxies = None):
    try:
        data = requests.get(url, timeout = 5,headers = headers)
        print(data.status_code)
    except requests.exceptions.ConnectionError as e:
        print('请求错误,url:',url)
        print('错误详情：',e)
        data = None
    except:
        print('未知错误,utl:',url)
        data = None
        
    if (data != None) and (500<=data.status_code<600):
        if (num_retries > 0):
            print('服务器错误，正在重试...')
            time.sleep(1)
            num_retries -=1
            get_data(url,num_retries, proxies = proxies)
    return data

#对网页内容解析
def parse_data(data):
    if data == None:
        return None
    charset = chardet.detect(data.content)
    data.encoding = charset['encoding']
    html_text = data.text
    
    
    interesting_data = re.findall('<title>(.*?)</title>', html_text)
    return interesting_data

if __name__ == '__main__':
    headers = get_headers()
    proxies = get_proxies()
    url = input('请输入网页链接：')
    data = get_data(url, num_retries = 3,proxies = proxies)
    interesting_data = parse_data(data)
    print(interesting_data)