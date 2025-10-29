import numpy as np
from scipy.optimize import linprog

c = np.array([0, 0, 0, 0, -1])

# (A) ########################################
Aeq1 = np.array([[1, 1, 1, 1, 1]])
beq1 = np.array([3])
bounds = [
    (0, None),   # x1 ≥ 0
    (0, None),   # x2 ≥ 0
    (0, None),   # x3 ≥ 0
    (None, 3),   # x4 ≤ 3 (ingen nedre grense spesifisert)
    (None, None) # x5 ubundet
]

Aub1 = np.array([[1, 0, 0, -1, 0]])
bub1 = np.array([4])
res = linprog(c, A_ub=Aub1, b_ub=bub1, A_eq=Aeq1, b_eq=beq1, bounds=bounds)# ikke forandre denne linja


# (B) #########################################
Aeq2 = np.array([[1, 1, 1, 1, 1]])
beq2 = np.array([3])
Aub2 = np.array([
    [-1,  0,  0,  0, 0],  # (i) x1 ≥ 0  -> -x1 ≤ 0
    [ 0, -1,  0,  0, 0],  # (i) x2 ≥ 0  -> -x2 ≤ 0
    [ 0,  0, -1,  0, 0],  # (i) x3 ≥ 0  -> -x3 ≤ 0
    [ 0,  0,  0,  1, 0],  # (iv) x4 ≤ 3
    [ 1,  0,  0, -1, 0],  # (iii) x1 - x4 ≤ 4
])
bub2 = np.array([0, 0, 0, 3, 4])
res2 = linprog(c, A_ub=Aub2, b_ub=bub2, A_eq=Aeq2, b_eq=beq2)# ikke forandre denne linja
