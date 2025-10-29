import numpy as np
from scipy.optimize import linprog

# Kostfunksjon
c = np.array([-2, -1, 0, 3, 0])

# Likhetsbetingelse
Aeq1 = np.array([[1, 1, 1, 1, 1]])
beq1 = np.array([6])

# Ulikheter
Aub1 = np.array([
    [-2, 0, 1, 0, -1],  # (ii) omskrevet
    [0, 1, 0, 1, 0],    # (iii)
    [1, 0, 0, 0, -1]    # (iv)
])
bub1 = np.array([-1, 4, 2])

# Grenser
bounds = [
    (0, None),
    (0, None),
    (None, None),
    (0, 3),
    (0, None)
]

# Løsning
res = linprog(c, A_ub=Aub1, b_ub=bub1, A_eq=Aeq1, b_eq=beq1, bounds=bounds)
print("Success:", res.success)
print("Optimal verdi:", res.fun)
print("x*:", res.x)
