import math
from unittest import TestCase
import numpy as np
import src.Algorithms.thomson_problem as th


class Test(TestCase):
    def test_random_points_on_sphere(self):
        for R in range(1, 3):

            points = th.random_points_on_sphere(10, R)
            for point in points:
                self.assertTrue(th.mag(point) - R < 0.0001)

    def test_normalise(self):
        point = np.array([2, 0, 0])
        self.assertTrue((th.normalise(point) == np.array([1, 0, 0])).all())

        point = np.array([1, 1, 1])
        self.assertTrue(
            th.mag(th.normalise(point)-np.array([1/math.sqrt(3), 1/math.sqrt(3), 1/math.sqrt(3)])) < 0.001)

        point = np.array([2, 1, 0])
        self.assertTrue(
            th.mag(th.normalise(point) - np.array([2 / math.sqrt(5), 1 / math.sqrt(5), 0])) < 0.001)

    def test_force(self): # Force is 1/d^2
        point0 = np.array([1, 0, 0])
        point1 = np.array([-1, 0, 0])
        self.assertTrue(
            th.mag(th.force(point0, point1) - np.array([0.25, 0, 0])) < 0.001
        )

    def test_thomson_force_step(self):
        point0 = np.array([1, 0, 0], dtype=float)
        point1 = np.array([-1, 0, 0], dtype=float)
        points = [point0, point1]
        th.thomson_force_step(points)
        self.assertTrue(
            th.mag(points[0] - np.array([1, 0, 0])) < 0.001
        )
        self.assertTrue(
            th.mag(points[1] - np.array([-1, 0, 0])) < 0.001
        )

    def test_periodic_force(self):
        point0 = np.array([0.3], dtype=float)
        point1 = np.array([0.2], dtype=float)
        boundary = np.array([1])
        self.assertTrue(
            th.mag(th.periodic_force(point0, point1, boundary) - np.array([100])) < 0.001
        )
        point0 = np.array([1.9], dtype=float)
        point1 = np.array([0.1], dtype=float)
        boundary = np.array([2])
        print(th.periodic_force(point0, point1, boundary))
        self.assertTrue(
            th.mag(th.periodic_force(point0, point1, boundary) - np.array([-1/(0.2*0.2)])) < 0.001
        )

    def test_thomson_flat_force_step(self):
        self.fail()