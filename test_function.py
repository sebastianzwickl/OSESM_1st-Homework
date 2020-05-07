# -*- coding: utf-8 -*-
"""
Created on Wed May  6 09:33:25 2020

@author: zwickl-nb
"""
from function import add
from function import validate


def test_add():
    assert add(2, 1) == 3


def test_validate():
    assert validate(20, 2) == 1
    

def only_renewable():
    assert only_renewable(100, 100) == 1

