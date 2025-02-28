import numpy as np

coords = np.array([
    [82, 76], [96, 44], [50, 5], [49, 8], [13, 7], [29, 89], [58, 30], [84, 39],
    [14, 24], [2, 39], [3, 82], [5, 10], [98, 52], [84, 25], [61, 59], [1, 65],
    [88, 51], [91, 2], [19, 32], [93, 3], [50, 93], [98, 14], [5, 42], [42, 9],
    [61, 62], [9, 97], [80, 55], [57, 69], [23, 15], [20, 70], [85, 60], [98, 5]
])

n = len(coords)

with open("distances.txt", "w") as f:
    f.write("DistanceMatrix:\n")
    
    for i in range(n):
        for j in range(n):
            distance = np.linalg.norm(coords[i] - coords[j])
            f.write(f"{i},{j},{distance:.2f}\n")