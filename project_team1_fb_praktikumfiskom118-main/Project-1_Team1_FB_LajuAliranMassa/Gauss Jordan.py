kelompok = """
Metode Gauss-Jordan
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

# gabungkan matriks A dan vektor b
AB = np.hstack((A, b.reshape(-1, 1)))

# tampilkan matriks awal
print("Matriks A:")
print(A)
print()
print("Matriks B:")
print(b)
print()
print("Matriks gabungan A dan B:")
print()
print(AB)

# proses eliminasi Gauss-Jordan
n = len(b)
for i in range(n):
    # membuat leading coefficient menjadi 1
    faktor = AB[i,i]
    AB[i] /= faktor
    
    # eliminasi ke bawah
    for j in range(i+1, n):
        faktor = AB[j,i] / AB[i,i]
        AB[j] -= faktor * AB[i]
    
    # eliminasi ke atas
    for j in range(i):
        faktor = AB[j,i] / AB[i,i]
        AB[j] -= faktor * AB[i]

# solusi
c = AB[:, -1]
print()
print("hasil:")
print(c)
