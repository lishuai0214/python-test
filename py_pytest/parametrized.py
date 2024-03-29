#!/usr/bin/env python3

import pytest

@pytest.mark.parametrize("data, expected", [((2, 3, 1, 4, 6), 1),
    ((5, -2, 0, 9, 12), -2), ((200, 100, 0, 300, 400), 0)])
def test_min(data, expected):

    val = min(data)
    print(val)
    assert val == expected

@pytest.mark.parametrize("data, expected", [((2, 3, 1, 4, 6), 6),
    ((5, -2, 0, 9, 12), 12), ((200, 100, 0, 300, 400), 400)])
def test_max(data, expected):
    val = max(data)
    print(val)
    assert val == expected