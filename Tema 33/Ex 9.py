import numpy as np
import pandas as pd

if __name__ == '__main__':

    data = {
        'Nume': ['Alexandru', 'Maria', 'Cristian', 'Elena', 'Florin'],
        'Vârstă': [28, 34, 22, 45, 30],
        'Oraș': ['București', 'Cluj-Napoca', 'Iași', 'Timișoara', 'Brașov']
    }

    df = pd.DataFrame(data)
    print(df)