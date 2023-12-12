kelompok = """
Metode Matrix Balikan
Kelompok 1
"""
print(kelompok)

import numpy as np

# definisikan matriks A dan b
A = np.array([[ 3600,  0,    0,     0,     -4000  ],
              [ -3600, 3600, 0,     0,     0      ],
              [ 0,    -3600, 3600,  0,     0      ],
              [ 0,     0,    -3600, 3600,  0      ],
              [ 0,     0,    0,     -3600, -400   ]], float)
b = np.array([-40, 0, 0, 0, 0], float)

# tampilkan matriks awal
print("Matriks awal:")
print(A)
print()

# hitung invers matriks A
A_inv = np.linalg.inv(A)

# tampilkan invers matriks A
print("Invers matriks A:")
for row in A_inv:
    print("[", "  ".join([f"{elem:8.5f}" for elem in row]), "]")
print()

# hitung solusi x
x = A_inv.dot(b)
print("Solusinya:")
print(x)
