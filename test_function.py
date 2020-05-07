# -*- coding: utf-8 -*-
"""
Created on Wed May  6 09:33:25 2020

@author: zwickl-nb
"""
from function import add
from function import validate
import pandas as pd

def test_add():
    assert add(2, 1) == 3


def test_validate():
    cap = {'c':50}
    cap = pd.DataFrame(cap, index=[0])
    demand = {'d':20}
    demand = pd.DataFrame(demand, index=[0])
    assert validate(cap, demand) == 1
    


