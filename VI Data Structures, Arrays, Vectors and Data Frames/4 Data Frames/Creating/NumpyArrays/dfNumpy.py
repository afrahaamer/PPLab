arr = np.array([[1, 2, 100],
                [2, 4, 100],
                [3, 8, 100]])

df_ = pd.DataFrame(arr, columns=['x', 'y', 'z'])

# modify the array
arr[0, 0] = 1000
df_ 