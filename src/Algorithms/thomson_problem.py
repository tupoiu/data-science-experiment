import math
import numpy as np
import random as rd

exponent_s = 2  # The exponent for the force


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
        return (target - repulsive_point)/math.pow(dist, exponent_s)


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


def pairwise_energy(point0: np.array, point1: np.array):
    dist = mag(point0 - point1)
    if dist == 0:
        return 0
    else:
        return 1 / math.pow(dist, exponent_s-1)


def thomson_energy(points: list[np.array]):
    E = 0
    n = len(points)
    for i in range(n):
        for j in range(i, n):
            E += pairwise_energy(points[i], points[j])

    return E
