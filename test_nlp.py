import pyomo.environ as pyo
import numpy as np
import time
from pyomo.environ import *
from pyomo.opt import SolverFactory

model = pyo.ConcreteModel()

model.x = pyo.Var(initialize = 0, bounds=(-5, 5))
model.y = pyo.Var(initialize = 0, bounds=(-5, 5))

x = model.x
y = model.y

# model.C1 = pyo.Constraint(expr= -x+2*y<=8)
# model.C2 = pyo.Constraint(expr= 2*x+y<=14)
# model.C3 = pyo.Constraint(expr= 2*x-y<=10)

model.obj = pyo.Objective(expr= cos(x+1) + cos(x) * cos(y), sense=maximize)

opt = SolverFactory('ipopt', executable='C:\\ipopt\\bin\\ipopt.exe')
opt.options['tol'] = 
opt.solve(model)

model.pprint()

x_value = pyo.value(x)
y_value = pyo.value(y)

print('x=', x_value)
print('y=', y_value)