# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 11:05:54 2020

@author: Vikto
"""

def listCustomersWithSales(sheet,sheet2):
    a={}
    for j in range(4,218888):
        i= sheet["K"+str(j)].value
        try:
            money=int(sheet["AC"+str(j)].value)
        except:
            print(j)
            
        if i in a:
            a[i]=a[i]+money
        else:
            a[i]=money
    return a