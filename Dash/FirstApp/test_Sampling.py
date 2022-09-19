from unittest import TestCase

import pandas as pd

import Sampling
from Algorithms import rabbit_problem
from Algorithms.rabbit_problem import Warren


def one():
    return 1


def concat(str1: str, str2: str):
    return str1 + str2


class Test(TestCase):
    def test_create_sample_to_array(self):
        results = Sampling.create_sample_to_array(method=one, args=[], trials=3)
        self.assertEqual(results, [1, 1, 1])

        results = Sampling.create_sample_to_array(method=concat, args=["lol", "epic"], trials=2)
        self.assertEqual(results, ["lolepic", "lolepic"])

    def test_create_sample_to_dataframe(self):
        results = Sampling.create_sample_to_dataframe(method=concat, args=["ok", "bro"], trials=4)
        expected_dataframe: pd.DataFrame = pd.DataFrame(columns=["Result"],
                                                        data=["okbro", "okbro", "okbro", "okbro"])
        comparison: pd.DataFrame = expected_dataframe == results
        self.assertTrue(comparison.iat[0, 0])
        self.assertTrue(comparison.iat[1, 0])
        self.assertTrue(comparison.iat[2, 0])
        self.assertTrue(comparison.iat[3, 0])

