import numpy as np

if __name__ == '__main__':
    x = int(input('Enter a number: '))
    a = np.zeros((x,x))
    for i in range(x):
        a[i,i] = 1
    print(a)