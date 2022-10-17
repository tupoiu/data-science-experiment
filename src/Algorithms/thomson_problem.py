import math
import numpy as np
import random as rd


def mag(x):
    return np.sqrt(x.dot(x))


def random_points_on_sphere(number: int, radius: float = 1) -> list:
    points = []

    for i in range(number):
        point = np.array([
            rd.normalvariate(0, 1),
            rd.normalvariate(0, 1),
            rd.normalvariate(0, 1)
        ])
        point = normalise(point)
        points += [radius*point]

    return points


def normalise(point: np.array):
    norm_sq = sum([point[i] * point[i] for i in range(3)])
    return point / math.sqrt(norm_sq)


def force(target: np.array, repulsive_point: np.array) -> np.array:  # Force on point0 from point 1
    dist = mag(target - repulsive_point)
    if dist == 0:
        return target - repulsive_point
    else:
        return (target - repulsive_point)/math.pow(dist, 2)


def thomson_force_step(points: list[np.array], learning_rate=0.001):
    n = len(points)
    forces = [0 for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            forces[i] += force(points[i], points[j])
            forces[j] += force(points[j], points[i])

    for i in range(n):
        points[i] += learning_rate*forces[i]
        points[i] = normalise(points[i])
