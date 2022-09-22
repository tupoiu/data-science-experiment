from unittest import TestCase

from src.Algorithms.russian_dolls import mergesort, compare_box, russian_doll_sort


class Test(TestCase):
    def test_mergesort(self):
        test_list = [0, 1]
        sorted_list = mergesort(test_list, lambda x, y: x < y, descending=False)
        self.assertEqual([0, 1], sorted_list)

        test_list = [0, 2, 1]
        sorted_list = mergesort(test_list, lambda x, y: x < y, descending=False)
        self.assertEqual([0, 1, 2], sorted_list)

        test_list = [0, 2, 4, 1, 0, 1]
        self.assertEqual(sorted(test_list), mergesort(test_list, lambda x, y: x < y, descending=False))
        self.assertEqual(False, mergesort(test_list, lambda x, y: -1, descending=True))

    def test_compare_box(self):
        box0 = [3, 8, 5]
        box1 = [4, 4, 2]
        self.assertEqual(0, compare_box(box0, box1))

        box0 = [8, 5, 1]
        box1 = [2, 2, 2]
        self.assertEqual(-1, compare_box(box0, box1))

        box0 = [3, 4, 5]
        box1 = [3, 6, 6]
        self.assertEqual(1, compare_box(box0, box1))

    def test_russian_doll_sort(self):
        boxes = [
            [4, 5, 8],
            [2, 7, 4],
            [6, 2, 3],
            [1, 1, 1]
        ]

        bad_boxes = [
            [9, 9, 1],
            [2, 2, 2],
        ]

        expected_boxes = [
            [1, 1, 1],
            [6, 2, 3],
            [2, 7, 4],
            [4, 5, 8]
        ]

        self.assertEqual(expected_boxes, russian_doll_sort(boxes, descending=False))
        expected_boxes.reverse()
        self.assertEqual(expected_boxes, russian_doll_sort(boxes, descending=True))
        self.assertEqual(False, russian_doll_sort(bad_boxes, descending=True))
        