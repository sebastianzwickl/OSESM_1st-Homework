# -*- coding: utf-8 -*-
"""
Created on Wed May  6 09:32:28 2020

@author: zwickl-nb
"""

# function from the lecture for testing
def add(a, b):
    return a + b


# check whether enough capacities are available
# note: yet not able to include a panda framework to test_validate
# that is why data type int is used in test_validate
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


# check whether enough renewable energy is available
# in this case: "priority feed" for renewable energy and no optimization is necessary
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

