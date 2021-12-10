#!/usr/bin/python2
from __future__ import print_function

import numpy as np

def validate(s, length):
    for cut_start in range(length):
        copy = np.roll(np.array(list(s)), cut_start)
        valid = True
        for cut in range(0, len(s), length):
            if (copy[0:length] != copy[cut:cut + length]).any():
                valid = False
        if valid:
            return True
    return False


def solution(s):
    # Brute force solution
    count = len(s)
    assert count > 0
    for length in range(1, count/2 + 1):
        if count % length != 0:
            continue
        if validate(s, length):
            return count / length

    return -1


def test_example1():
    s = "abcabcabcabc"
    assert solution(s) == 4


def test_example2():
    s = "abccbaabccba"
    assert solution(s) == 2

def test_same_character():
    s = "xxxxxxxxxx"
    assert solution(s) == len(s)

def test_example1_rotated():
    s = "cabcabcabcab"
    assert solution(s) == 4

