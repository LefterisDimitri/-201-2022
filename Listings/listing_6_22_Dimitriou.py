#Listing 6.22 : Calculate quantum entangled states

from scipy import linalg as LA
import numpy as np


nmax = 4

H = np.zeros((nmax, nmax), float)

XAXB = np.array([[0,0,0,1], [0,0,1,0], [0,1,0,0], [1,0,0,0]])
YAYB = np.array([[0,0,0,-1], [0,0,1,0], [0,1,0,0], [-1,0,0,0]])
ZAZB = np.array([[1,0,0,0], [0,-1,0,0], [0,0,-1,0], [0,0,0,1]])
SASB = XAXB + YAYB + ZAZB - 3*ZAZB  # Hamiltonian
print('\nHamiltonian without mu~2/r~3 factor \n', SASB, '\n')

es, ev = LA.eig(SASB)  # Eigenvalues and eigenvectors
print('Eigenvalues\n', es, '\n')
print("Eigenvectors (in columns)\n", ev, "\n")
phil = (ev[0, 0], ev[1, 0], ev[2, 0], ev[3, 0])  # Bigenvectors
phi4 = (ev[0, 1], ev[1, 1], ev[2, 1], ev[3, 1])
phi3=(ev[0, 2], ev[1, 2], ev[2, 2], ev[3, 2])
phi2=(ev[0, 3], ev[1, 3], ev[2, 3], ev[3, 3])
basis=[phil, phi2, phi3, phi4]  # List eigenvectors

for i in range(0, nmax):  # Hamiltonian in new basis
    for j in range(0, nmax):
        term = np.dot(SASB, basis[i])
        H[i, j] = np.dot(basis[j], term)

print('Hamiltonian in Eigenvector Basis\n', H)
