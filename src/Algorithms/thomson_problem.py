import math
import numpy as np
import random as rd

exponent_s = 1  # The exponent for the energy (exponent for force is 1+exponent_s)


def mag(x):
    return np.sqrt(x.dot(x))


def mag2(x):
    return x.dot(x)


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
    norm_sq = sum([point[i] * point[i] for i in range(len(point))])
    return point / math.sqrt(norm_sq)


def force(target: np.array, repulsive_point: np.array) -> np.array:  # Force on target from repulsive force
    dist = mag(target - repulsive_point)
    if dist == 0:
        return target - repulsive_point
    else:
        return (target - repulsive_point)/math.pow(dist, exponent_s+2)  # +1 from differentiating, +1 from normalising


def periodic_force(target: np.array, repulsive_point: np.array, boundary: np.array) -> np.array:  # 2D Flat torus force
    # | x y     | : abs(x - y)            : |x-y|<= boundary/2 : wrap = 0
    # | x     y | : abs(x + boundary - y) : y - x > boundary/2 : wrap = 1
    # | y     x | : abs(x - boundary - y) : x - y > boundary/2 : wrap = -1
    wrap = np.array([
        int(target[i] - repulsive_point[i] < -boundary[i]/2) - int(target[i] - repulsive_point[i] > boundary[i]/2)
        for i in range(len(target))
    ])
    diff = target - repulsive_point + boundary*wrap
    dist = mag(diff)
    if dist == 0:
        return target - repulsive_point
    else:
        return diff/math.pow(dist, exponent_s+2)
        # s+2: +1 from differentiating, +1 from normalising


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


def thomson_flat_force_step(points: list[np.array], boundary: list, learning_rate=0.001):
    n = len(points)
    forces = [0 for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            forces[i] += periodic_force(points[i], points[j], boundary)
            forces[j] += periodic_force(points[j], points[i], boundary)

    for i in range(n):
        points[i] += learning_rate*forces[i]
        for cpnt, j in enumerate(points[i]):  # Push each component back onto the representative domain
            points[i][j] += (cpnt < 0) * boundary[j] - (cpnt > boundary[j]) * boundary[j]


def pairwise_energy(point0: np.array, point1: np.array):
    dist = mag(point0 - point1)
    if dist == 0:
        return 0
    else:
        return 1 / math.pow(dist, exponent_s)


def thomson_energy(points: list[np.array]):
    E = 0
    n = len(points)
    for i in range(n):
        for j in range(i, n):
            E += pairwise_energy(points[i], points[j])

    return E
