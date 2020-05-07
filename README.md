# Open Source Modeling
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
# easy linear program (LP) 

LP for the supply of the electricity demand. 
available technologies (wind, nuclear, coal, gas)

Approach of the program 
1) read in data from excel file data.xlsx
2) validate and check the data 
3) optimization of the linear program 

Description of files:
- data.xlsx: input data for marginal costs, intermittent supply and demand 
- function.py: contains functions (e.g. validate, only_renewable)
- optimization_file.py: linear program (LP) 
- test_function.py: checks the functions in function.py

Description of functions:
- cost_rule: objective function, minimize costs of supply
- demand_rule: supply must be equal or greater than demand
- cap_rule: upper bound for capacities
- validate: check the input data. result: solvable or not
- only_renewable: checks whether only wind can supply the demand
