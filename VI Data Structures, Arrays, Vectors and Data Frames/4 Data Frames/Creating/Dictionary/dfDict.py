import numpy as np
import pandas as pd

d = {'x': [1, 2, 3], 'y': np.array([2, 4, 8]), 'z': 100}

pd.DataFrame(d)

# Control the index and order
pd.DataFrame(d, index=[100, 200, 300], columns=['z', 'y', 'x'])
