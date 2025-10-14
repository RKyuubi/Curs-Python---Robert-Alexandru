import numpy as np

if __name__ == '__main__':
    a = np.random.randint(0,21, size=(4,4))
    val_max = np.max(a)
    val_min = np.min(a)
    print(a)
    print(val_max)
    print(val_min)

    val_max_index = np.where(a == val_max)
    val_min_index = np.where(a == val_min)
    print(val_max_index)
    print(val_min_index)