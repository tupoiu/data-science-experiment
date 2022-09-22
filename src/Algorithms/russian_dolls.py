import math


# Given an array of 3-vectors such that arr[0] = [4, 6, 5], sort that array st that the boxes fit within one
# another or return false if they can't.

def mergesort(array: list, comparison, descending) -> list or bool:
    if len(array) == 1:
        return array
    if len(array) == 2:
        higher = comparison(array[0], array[1])
        if higher == -1:
            return False
        elif higher == descending:
            return [array[1], array[0]]
        elif higher == 1 - descending:
            return array
    middle = math.floor(len(array)/2)
    first_half = array[0:middle]
    second_half = array[middle:len(array)]
    sorted1 = mergesort(first_half, comparison, descending=descending)
    sorted2 = mergesort(second_half, comparison, descending=descending)

    return merge(sorted1, sorted2, comparison, descending=descending)


def merge(sorted0: list, sorted1: list, comparison, descending):
    if sorted0 is False or sorted1 is False:
        return False
    size = len(sorted0) + len(sorted1)
    cursor0 = 0
    cursor1 = 0
    array: list = []
    for i in range(size):
        higher = comparison(sorted0[cursor0], sorted1[cursor1])
        if higher == -1:
            return False
        elif higher == descending:
            array.append(sorted1[cursor1])
            cursor1 += 1
        elif higher == 1-descending:
            array.append(sorted0[cursor0])
            cursor0 += 1

        if cursor0 == len(sorted0):
            return array + sorted1[cursor1:len(sorted1)]
        if cursor1 == len(sorted1):
            return array + sorted0[cursor0:len(sorted0)]

    return array


def russian_doll_sort(boxes: list, descending):
    return mergesort(boxes, compare_box, descending=descending)


def compare_box(box0: list[int], box1: list[int]) -> int or bool:  # Returns the index of the bigger box
    winning = -1
    dim = len(box0)
    b0 = sorted(box0)
    b1 = sorted(box1)
    for i in range(dim):
        diff = b0[i] - b1[i]
        if diff < 0:
            if winning == 0: return -1
            winning = 1

        if diff > 0:
            if winning == 1: return -1
            winning = 0

    return 0 if winning == -1 else winning
