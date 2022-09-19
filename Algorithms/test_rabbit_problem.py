from unittest import TestCase

from Algorithms import rabbit_problem
from Algorithms.rabbit_problem import Warren


class TestWarren(TestCase):
    def test_guess(self):
        warren = Warren(2)
        g1 = warren.guess(0)
        g2 = warren.guess(0)
        self.assertEqual(True, bool(g1) ^ bool(g2))


class TestRabbitSearch(TestCase):
    def test_algo(self):
        found_every_rabbit = True
        for i in range(100):
            warren = Warren(100+i, True)
            found_every_rabbit = found_every_rabbit and rabbit_problem.rabbit_search(warren) > 0
        self.assertTrue(found_every_rabbit)
