import numpy as np

if __name__ == '__main__':
    vector = np.arange(1,13)
    matrice_3x4 = vector.reshape((3,4))
    print(matrice_3x4)
    matrice_transpusa = matrice_3x4.T
    print(matrice_transpusa)