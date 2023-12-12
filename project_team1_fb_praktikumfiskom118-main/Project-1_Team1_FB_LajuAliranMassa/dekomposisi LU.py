kelompok = """
Metode Dekomposisi LU
Kelompok 1
"""
print(kelompok)

import numpy as np
from scipy.linalg import lu_factor, lu_solve

A = np.array([[ 3600,  0,    0,     0,     -4000  ],
              [ -3600, 3600, 0,     0,     0      ],
              [ 0,    -3600, 3600,  0,     0      ],
              [ 0,     0,    -3600, 3600,  0      ],
              [ 0,     0,    0,     -3600, -400   ]])
B = np.array([-40, 0, 0, 0, 0])

n = A.shape[0]

# Inisialisasi matriks L dan U dengan nol
L = np.zeros((n, n))
U = np.zeros((n, n))

# Iterasi untuk menghitung matriks L dan U
for k in range(n):
    L[k, k] = 1.0
    for i in range(k+1):
        U[i, k] = A[i, k] - np.dot(L[i, :i], U[:i, k])
    for i in range(k+1, n):
        L[i, k] = (A[i, k] - np.dot(L[i, :k], U[:k, k])) / U[k, k]

    print(f'Iterasi ke-{k+1}')
    
    print('Matriks L: ')
    print(L)
    print()
    print('Matriks U: ')
    print(U)
    print()

# Menyelesaikan sistem persamaan linear Ax = B
LU, piv = lu_factor(A)
x = lu_solve((LU, piv), B, overwrite_b=True)

print("hasil: ")
print(x)

assert np.allclose(A @ x, B)
