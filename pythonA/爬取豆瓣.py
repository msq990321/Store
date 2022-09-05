# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 20:48:55 2022

@author: Administrator
"""

##豆瓣
import requests
import pandas as pd
from bs4 import BeautifulSoup

#requests
def get_data():
    headers ={'User-Agent':'Mozilla/5.0'}
    url = 'https://book.douban.com'
    res = requests.get(url,headers=headers,verify=True,timeout=30)#UA伪装
    res.raise_for_status()
    res.enconding='utf-8'
    return res

#内容进一步提取
def parse_data(res):
    soup = BeautifulSoup(res.text,'lxml')
    books = soup.find('ul',{'class':'list-col list-col5 list-express slide-item'})
    books = books.find_all('li')#返回一个列表，具有强大的属性
#获取进一步信息
    img_urls=[]
    authors=[]
    titles=[]
    abstracts=[]
    for book in books:
        #图书封面url
        img_url = book.find_all('a')[0].find('img').get('src')
        img_urls.append(img_url)
        #图书标题
        title = book.find('h4').get_text()
        title = title.replace('\n','').replace(' ','')
        titles.append(title)
        #abstracts
        abstract = book.find('p',{'class':'abstract'}).get_text()
        abstract = abstract.replace('\n','').replace(' ','')
        abstracts.append(abstract)
        #author
        author = book.find('span',{'class':'author'}).get_text()
        author = author.replace('\n','').replace(' ','')
        authors.append(author)
    return img_urls,authors,titles,abstracts

def save_data(img_urls,authors,titles,abstracts):
#pandas存储数据
    result = pd.DataFrame()
    result["img_urls"] = img_urls
    result["authors"] = authors
    result["titles"] = titles
    result['abstracts'] = abstracts
    result.to_csv('result.csv',index = None,encoding='utf-16')
    
def run():
    res = get_data()
    img_urls,authors,titles,abstracts = parse_data(res)
    save_data(img_urls,authors,titles,abstracts)    
    
if __name__ == '__main__':
    run()