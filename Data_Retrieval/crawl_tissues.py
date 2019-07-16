#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 14:24:26 2019

@author: MDIBL\20pbenson
"""

import fetch_genes as fg

tissues = ['full_blood', 'kidney', 'pancreas', 'monocytes', 'all', 'pdac', 'prcc', 'hlf']
tissue_dict = {}

for tissue in tissues:
    url = "http://tools.genxpro.net/apadb/browse/human/" + str(tissue) + "/?page=1"
    pages = fg.get_pages(url)
    
    tissue_dict[tissue] = fg.crawl_pages(pages, str(tissue))
    
    