import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.optimize import linprog
obj = [-1, -2]
#      ─┬  ─┬
#       │   └┤ Coeficiente de  y
#       └────┤ Coeficiente de  x
lhs_ineq = [[ 2,  1],  # lado izquierdo de la restricción 1
            [-4,  5],  # lado izquierdo de la restricción 2
            [ 1, -2]]  # lado izquierdo de la restricción 3
rhs_ineq = [20,  # lado derecho de la restricción 1
            10,  # lado derecho de la restricción 2
             2]  # lado derecho de la restricción 3
lhs_eq = [[-1, 5]]  # lado izquierdo de la restricción 4
rhs_eq = [15]       # lado derecho de la restricción 4
bnd = [(0, float("inf")),  # naturaleza de x
        (0, float("inf"))]  # naturaleza de y
opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,
              A_eq=lhs_eq, b_eq=rhs_eq, bounds=bnd,
              method="revised simplex") #se puede usar "simplex" o "interior point"
print (opt)