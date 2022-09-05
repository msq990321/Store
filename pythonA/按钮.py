# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 15:54:20 2022

@author: Administrator
"""


import easygui as g

msg = "请填写一下信息(其中带*号的项为必填项)"
title = "relative files"
fieldNames = ["input pdb ","mdp","123","*手机号码","QQ","*Email"]
fieldValues = []
fieldValues = g.multenterbox(msg,title,fieldNames)
#print(fieldValues)
while True:
    if fieldValues == None :
        break
    errmsg = ""
    for i in range(len(fieldNames)):
        option = fieldNames[i].strip()
        if fieldValues[i].strip() == "" and option[0] == "*":
            errmsg += ("【%s】为必填项   " %fieldNames[i])
    if errmsg == "":
        break
    fieldValues = g.multenterbox(errmsg,title,fieldNames,fieldValues)
print("您填写的资料如下:%s" %str(fieldValues))