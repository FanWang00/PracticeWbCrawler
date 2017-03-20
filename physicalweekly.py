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


def content_cri(tag):
    #return re.compile('wsite-menu-subitem').search(class_) and href 
    pass
    
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
    # #print(link_new[i])
    

def get_pdf_link(link):
    j = 0 
    content_pdf = []
    response_temp = requests.get(link)
    soup_temp = BeautifulSoup(response_temp.text,'lxml')
    #content_pdf_temp = soup_temp.find_all('a', href = True)
    content_pdf_temp = soup_temp
    while (content_pdf_temp.get.endswith('.pdf')):
        content_pdf.append(content_pdf_temp[j].get('href'))
        j += 1
        print(content_pdf[j])
    
    
get_pdf_link(link_new[3])

'''
for j in link_new:
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