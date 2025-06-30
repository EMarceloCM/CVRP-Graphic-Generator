import math

# Coordenadas atualizadas (indexadas de 0 a 31)
coordinates = {
    0: (82, 76), 1: (96, 44), 2: (50, 5), 3: (49, 8), 4: (13, 7), 5: (29, 89),
    6: (58, 30), 7: (84, 39), 8: (14, 24), 9: (2, 39), 10: (3, 82), 11: (5, 10),
    12: (98, 52), 13: (84, 25), 14: (61, 59), 15: (1, 65), 16: (88, 51), 17: (91, 2),
    18: (19, 32), 19: (93, 3), 20: (50, 93), 21: (98, 14), 22: (5, 42), 23: (42, 9),
    24: (61, 62), 25: (9, 97), 26: (80, 55), 27: (57, 69), 28: (23, 15), 29: (20, 70),
    30: (85, 60), 31: (98, 5)
}

def euclidean_distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def total_distance(solution, coordinates):
    total = 0.0
    for route in solution:
        for i in range(len(route) - 1):
            a = coordinates[route[i]]
            b = coordinates[route[i + 1]]
            total += euclidean_distance(a, b)
    return total

solution = [
    [0, 21, 31, 19, 17, 13, 7, 26, 0],
    [0, 12, 1, 16, 30, 0],
    [0, 27, 24, 0],
    [0, 29, 18, 8, 9, 22, 15, 10, 25, 5, 20, 0],
    [0, 14, 28, 11, 4, 23, 3, 2, 6, 0]
]

print("Total distance:", total_distance(solution, coordinates))