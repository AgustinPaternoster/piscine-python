import numpy as np

tmp = [
        [8, 3, 5],
        [10, 1, 7],
        [4, 9, 2],
        [6, 5, 8]
    ]

result = [
        [8, 10, 4, 6],
        [3, 1, 9, 5],
        [5, 7, 2, 8]
    ]

img = np.array(tmp)

col, row = img.shape

newimg = np.zeros((row,col))

for c in range(col):
    for r in range(row):
        newimg[r][c] = img[c][r]

print(newimg)
