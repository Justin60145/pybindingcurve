"""Simulation example 1:1 binding"""

import numpy as np
import pybindingcurve as pbc
import time

# Show the difference in speed between a kinetic solution and the highly efficient direct analytical method for 1:1 binding
start = time.time()
print(
    f"One to one binding test analytical\t\tpl={pbc.System_analytical_one_to_one_pl().query({'p':4, 'l':10,'kdpl':1})}, \ttook {round(time.time()-start,5)} seconds")
start = time.time()
print(f"One to one binding test kinetic  \tpl={pbc.System_kinetic_one_to_one_pl().query({'p':4, 'l':10,'kdpl':1})}, \ttook {round(time.time()-start,5)} seconds")

 # Simulate a binding curveñ
system_parameters = {'p': np.linspace(0, 10), 'l': 10, 'kdpl': 1}
mySystem = pbc.BindingCurve("1:1")
mySystem.add_curve(system_parameters)
mySystem.show_plot()
