# -*- coding: utf-8 -*-
"""
Created on Wed May  6 09:32:28 2020

@author: zwickl-nb
"""


def add(a, b):
    return a + b


def validate(cap, d):
    if type(cap) == int and type(d) == int:
        capacities = cap
        demand = d
    else:
        capacities = sum(sum(cap.values))
        demand = sum(d.values)
    if capacities >= demand:
        return 1
    else:
        return 0


def only_renewable(cap, d):
    if type(cap) == int and type(d) == int:
        if cap > d:
            return 1
        else:
            return 0
    else:
        if cap['wind'][0] >= d.values:
            return 1
        else:
            return 0
