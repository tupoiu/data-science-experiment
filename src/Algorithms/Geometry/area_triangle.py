import numpy as np

mag = lambda x: np.sqrt(x.dot(x))


def area_of_triangle(points: list[np.array]):
    points = [
        np.array(points[0]),
        np.array(points[1]),
        np.array(points[2])
    ]
    AB = points[1] - points[0]  # The vector from vertex A to vertex B
    BC = points[2] - points[1]
    return mag(np.cross(AB, BC))/2


def dot(vec1: list[float], vec2: list[float]):
    dot_prod = 0
    for i in range(len(vec1)):
        dot_prod += vec1[i]*vec2[i]
    return dot_prod
