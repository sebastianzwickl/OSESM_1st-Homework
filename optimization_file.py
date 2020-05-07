# -*- coding: utf-8 -*-
"""
Created on Wed May  6 15:00:18 2020

@author: zwickl-nb
"""

import pandas as pd
import pyomo.environ as py
from function import validate


def cost_rule(m):
     costs = 0
     for i in indexlist:
        costs += model.x[i] * m.frame[i][0]
     return costs


def demand_rule(m):
    supply = 0
    for i in indexlist:
        supply += m.x[i]
    return supply >= m.demand[0]


def cap_rule(m, i):
    return m.x[i] <= m.inter[i][0]
    


mc = pd.read_excel('data.xlsx','marginal costs', index=False)
mc.reset_index(drop=True)
demand = pd.read_excel('data.xlsx', 'demand')
inter = pd.read_excel('data.xlsx', 'intermittent')

if validate(inter, demand):
    model = py.ConcreteModel()
    model.frame = mc
    model.demand = demand.values[0]
    model.inter = inter

    mc_dict = mc.to_dict()
    indexlist = set()
    
    for key in mc_dict:
        indexlist.add(key)

    model.il = indexlist 
    model.x = py.Var(indexlist, within = py.NonNegativeReals)
    model.c1 = py.Constraint(rule = demand_rule,
                             doc='Supply equals demand')
    model.c2 = py.Constraint(model.il, rule = cap_rule,
                             doc='intermittent supply and capacities')
    model.obj = py.Objective(rule = cost_rule,
                             sense = py.minimize,
                             doc='minimize costs of supply')
    opt = py.SolverFactory('glpk')
    opt.solve(model)
    for i in indexlist:
        print(i,':',model.x[i].value)

