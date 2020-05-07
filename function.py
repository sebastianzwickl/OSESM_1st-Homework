# -*- coding: utf-8 -*-
"""
Created on Wed May  6 09:32:28 2020

@author: zwickl-nb
"""


def add(a, b):
    return a + b


def validate(cap, demand):
    capacities = sum(sum(cap.values))
    if capacities >= sum(demand.values):
        return 1
    else:
        return 0
