#!/usr/bin/env python
import pytest

def test_one():  # <1>
    print("WHOOPEE")
    assert(1)

def test_two(common_fixture):   # <2>
    assert(common_fixture == "DATA")

if __name__ == '__main__':
    pytest.main([__file__, "-s"])   # <3>

