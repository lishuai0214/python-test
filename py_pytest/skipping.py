#!/usr/bin/env python3

import pytest

@pytest.mark.skip(reason='out-of-date api')
def test_min():
    values = (2, 3, 1, 4, 6)

    val = min(values)
    assert val == 1

def test_max():
    values = (2, 3, 1, 4, 6)

    val = max(values)
    assert val == 6