kelompok = """
Metode Gauss Naive
Kelompok 1
"""
print(kelompok)

import numpy as np
import sys

# Matriks koefisien
A = np.array([[ 3600,  0,    0,     0,     -4000  ],
              [ -3600, 3600, 0,     0,     0      ],
              [ 0,    -3600, 3600,  0,     0      ],
              [ 0,     0,    -3600, 3600,  0      ],
              [ 0,     0,    0,     -3600, -400   ]])

# Vektor hasil
b = np.array([-40, 0, 0, 0, 0])

# Jumlah variabel
n = len(b)

# Matriks gabungan A dan b
AB = np.concatenate((A, np.reshape(b, (n, 1))), axis=1)

# Menampilkan matriks A, b, dan gabungan AB
print("Matriks A:\n", A, "\nVektor b:\n", b, "\n")
print("Matriks gabungan:\n", AB)

# Inisialisasi vektor solusi
c = np.zeros(n)

# Eliminasi Gauss
for i in range(n):
    # Cek apakah terdapat pembagian dengan nol
    if AB[i][i] == 0.0:
        sys.exit('Terdeteksi pembagian dengan nol')

    for j in range(i+1, n):
        # Rasio pengurangan baris
        ratio = AB[j][i]/AB[i][i]

        for k in range(n+1):
            # Pengurangan baris
            AB[j][k] = AB[j][k] - ratio * AB[i][k]

# Substitusi mundur
c[n-1] = AB[n-1][n]/AB[n-1][n-1]

for i in range(n-2,-1,-1):
    c[i] = AB[i][n]

    for j in range(i+1,n):
        c[i] = c[i] - AB[i][j]*c[j]

    c[i] = c[i]/AB[i][i]

# Menampilkan solusi
print("hasil: ")
print(c)
