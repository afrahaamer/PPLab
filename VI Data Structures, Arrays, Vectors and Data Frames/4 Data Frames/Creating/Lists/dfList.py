l = [{'x': 1, 'y': 2, 'z': 100},
    {'x': 2, 'y': 4, 'z': 100},
    {'x': 3, 'y': 8, 'z': 100}]

pd.DataFrame(l)

l = [[1, 2, 100],
    [2, 4, 100],
    [3, 8, 100]]
    
pd.DataFrame(l, columns=['x', 'y', 'z'])