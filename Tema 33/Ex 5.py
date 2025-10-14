import numpy as np

if __name__ == '__main__':
    a = np.array([1,2,3])
    b = np.array([4,5,6])
    suma = a+b
    produs = a*b
    produs_scalar=a.dot(b)
    putere = a**2
    print(suma)
    print(produs)
    print(produs_scalar)
    print(putere)