from unittest import TestCase

import numpy as np

from src.Algorithms.Geometry.area_triangle import dot, area_of_triangle


class Test(TestCase):
    def test_dot(self):
        v1 = [0, 2, 4]
        v2 = [13, -1, 3]
        self.assertEqual(0 -2 + 12, dot(v1, v2))

    def test_area_triangle(self):
        a = [0, 0]
        b = [4, 0]
        c = [0, 5]
        self.assertEqual(10, area_of_triangle([a, b, c]))

        a = np.array([0, 5])
        b = np.array([0, 0])
        c = np.array([4, 0])
        self.assertEqual(10, area_of_triangle([a, b, c]))

        a = np.array([4, 5, -5])
        b = np.array([4, 0, -5])
        c = np.array([4, 0, -9])
        self.assertEqual(10, area_of_triangle([a, b, c]))
