#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 00:43:40 2017

@author: wf
"""

import requests
from bs4 import BeautifulSoup
import re
import shutil

start_link = 'http://physikmethoden.weebly.com'

content_list1 = []


    
def get_link(start_link):
    response = requests.get(start_link)
    soup = BeautifulSoup(response.text,'lxml')
    content_list_temp = soup.find_all('a',class_=['wsite-menu-subitem', 'wsite-menu-item'])
    # print(content_list_temp)
    content_list = []
    for link in content_list_temp:
        content_list.append(link.get('href'))
        # print(soup)
    # #print(content_list)
    return (content_list)

#def combine_link(start_link)
content_list = get_link(start_link)
link_new = []
for i in range(len(content_list)):
    link_new.append(start_link+str(content_list[i]))
    #print(link_new[i])


def Download_file(start_link, original_link):
    response = requests.get(start_link)
    soup = BeautifulSoup(response.text,'lxml')
    content_list_temp = soup.find_all('a', href=True)
    # print(content_list_temp)
    for link in content_list_temp:
        if link.get('href').endswith('.pdf'):    
            content_list1.append(original_link+link.get('href'))
        #content_list1.append(link)
        # print(soup)
            #print(content_list1)
    return content_list1

  
down_pdf_list=[]
#get_link2(link_new[3],start_link)
for down_link in link_new:
    down_pdf_list = Download_file(down_link, start_link)
    down_pdf_list += down_pdf_list
    print(down_pdf_list)
#print(down_pdf_list)
print(down_pdf_list)
print('link fetch complete, download start')

'''
page = 0
for j in down_pdf_list:
    response = requests.get(j, stream=True)
    try:    
        with open('img'+str(page)+'.pdf', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
    except ConnectionResetError as err:
        print(r'connetcion erro', err)
    finally:
        print('ok')
    page += 1
    del response
'''