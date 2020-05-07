# -*- coding: utf-8 -*-
"""
Created on Wed May  6 09:32:28 2020

@author: zwickl-nb
"""
from pyomo.environ import *
import numpy as np


def add(a, b):
    return a + b

#def validation(a,b,c):
#    if bool((bool(a) + bool(b) + bool(c))):
#        return True
#    else:
#        return False

#def optimize(mc, demand):
#    model = ConcreteModel()
#    mc_dict = mc.to_dict()
#    indexlist = set()
#    
#    for key in mc_dict:
#        indexlist.add(key)
#
#    model.d = demand.values
#    
#    
#
#    model.c = Param(indexlist, initialize = mc_dict)
#    print(model.c.__call__)
#
#    model.x = Var(indexlist, within = NonNegativeReals)

#    model.c1 = Constraint(expr = model.x[1] >= model.d)
#    model.obj = Objective(
#            expr = model.x[1] ,sense = minimize)
#    opt = SolverFactory('glpk')
#    opt.solve(model)
#    print(model.x[1].value)
#    return    
