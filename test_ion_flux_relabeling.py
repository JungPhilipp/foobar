#!/usr/bin/python2
from __future__ import print_function


import numpy as np


def traverse(height, start, search):
    current = -1
    if height == 1:
        current = start + 1
    else:
        left = traverse(height - 1, start, search)
        right = traverse(height - 1, left, search)
        current = right + 1
        if left in search:
            search[left] = current
        if right in search:
            search[right] = current

    return current


def solution(height, nodes):
    search = dict()
    for node in nodes:
        search[node] = -1
    traverse(height, 0, search)
    return [search[key] for key in nodes]


def test_example1():
    assert solution(5, [19, 14, 28]) == [21, 15, 19]


def test_example2():
    assert solution(3, [7, 3, 5, 1]) == [-1, 7, 6, 3]


if __name__ == "__main__":
    print(solution(3, [7, 3, 5, 1]))
