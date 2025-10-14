import numpy as np

if __name__ == '__main__':
    vector = np.random.randint(0,51,size=10)
    elemente_mari = []

    for element in vector:
        if element > 25:
            elemente_mari.append(element)

    print(vector)
    vector_nou = np.array(elemente_mari)
    print(vector_nou)