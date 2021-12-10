#!/usr/bin/python2
from __future__ import print_function

import numpy as np


def solution(x, y):
    side = x + y -1
    result = (side*side - side) / 2 + x
    return str(result)


def test_example1():
    assert solution(3, 2) == "9"


def test_example2():
    assert solution(5, 10) == "96"

