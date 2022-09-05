# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 15:50:10 2022

@author: Administrator
"""


import time 
def printtime(func):
    def wrapper(*args,**kwargs):
        print(time.ctime())
        return func(*args,**kwargs)
    
    return wrapper()

@printtime
def printhello(name):
    print('Hello', name)
    
if __name__ == '__main__':
    printhello_plus=printtime(printhello)
    printhello('Sam')