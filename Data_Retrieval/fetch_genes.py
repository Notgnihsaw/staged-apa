# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import re

def apadb_to_df(url):
    html = urlopen(url)
    
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.findAll("table", {'class':'paleblue'})[0]
    rows = table.findAll("tr")
    
    rows_cont = [None]
    for k in range(len(rows)):
        rows_cont.append(rows[k].contents)
        
    for i in range(1, len(rows_cont)):
        for j in range(rows_cont[i].count('\n')):
            rows_cont[i].remove('\n')
            
    row_strings = rows_cont.copy()
    
    del row_strings[0]
    
    for i in range(len(row_strings)):
        for j in range(len(row_strings[i])):
            row_strings[i][j] = row_strings[i][j].string
            
    col_headers = row_strings[0]
    
    row_strings = row_strings[1:len(row_strings)]
    
    apadb_df = pd.DataFrame(row_strings, columns=col_headers)
    
    return apadb_df

def get_pages(url):
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    
    page_list = soup.findAll("li", {'class':'cardinality'})
    
    page_list = page_list[0].string
    page_list = page_list.strip()
    page_list = re.sub('Page [0-9]{1,3} of ', '', page_list)
    
    return int(page_list)

#print(get_pages("http://tools.genxpro.net/apadb/browse/human/full_blood/?page=1"))

def crawl_pages(page_end, tissue):
    full_df = pd.DataFrame()
    
    for page in range(1, page_end):
        feed_url = "http://tools.genxpro.net/apadb/browse/human/" + tissue + "/?page=" + str(page)
        full_df = full_df.append(apadb_to_df(feed_url))
    
    return full_df

