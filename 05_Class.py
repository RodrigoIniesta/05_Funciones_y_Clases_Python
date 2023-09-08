# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 09:02:10 2023

@author: MRDV
"""

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy
import importlib
from scipy.stats import skew,kurtosis,chi2

data_type = 'simulacion' #simulacion real custom
variable_name = 'normal' #normal,student,...
dm = class_distribution_manager()  #we are creating a "class"
dm.load_timeseries(data_type,variable_type,bool_plot=True)
dm.compute()
dm.hitogram() 
print(dm)

def test(a,b):
    return a+b

x=test(1,2)
np.random.normal()
print(x)

class Instrument:
    def __init__(self,asset,underlying):
        self.asset=asset
        self.underlying=underlying

test=Instrument('swap', 'tiie') 
print(f'prueba de {test.asset} a ver si jala')
