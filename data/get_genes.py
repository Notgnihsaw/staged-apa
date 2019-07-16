#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 15:49:53 2019

@author: CORP\20pbenson
"""

import pickle
import pandas as pd

tissue_dict = pickle.load(open('../../staged-apa_data/tissue_dict.pickle', 'rb'))

tissues = ['full_blood', 'kidney', 'pancreas', 'monocytes', 'all', 'pdac', 'prcc', 'hlf']

for tissue in tissues:
    tissue_dict[tissue]['sites'] = tissue_dict[tissue]['PolyA Sites']

full_blood_df = tissue_dict['full_blood']
full_blood_df['tissue'] = 'full_blood'
kidney_df = tissue_dict['kidney']
kidney_df['tissue'] = 'kidney'
pancreas_df = tissue_dict['pancreas']
pancreas_df['tissue'] = 'pancreas'
monocytes_df = tissue_dict['monocytes']
monocytes_df['tissue'] = 'monocytes'
all_df = tissue_dict['all']
all_df['tissue'] = 'all'
pdac_df = tissue_dict['pdac']
pdac_df['tissue'] = 'pdac'
prcc_df = tissue_dict['prcc']
prcc_df['tissue'] = 'prcc'
hlf_df = tissue_dict['hlf']
hlf_df['tissue'] = 'hlf'

complete_df = pd.DataFrame()
complete_df = complete_df.append(full_blood_df)
complete_df = complete_df.append(kidney_df)
complete_df = complete_df.append(pancreas_df)
complete_df = complete_df.append(monocytes_df)
complete_df = complete_df.append(all_df)
complete_df = complete_df.append(pdac_df)
complete_df = complete_df.append(prcc_df)
complete_df = complete_df.append(hlf_df)