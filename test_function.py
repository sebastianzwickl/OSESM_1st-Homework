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
    assert validate(50, 20) == True