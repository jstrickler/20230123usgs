#!/usr/bin/env python
import pytest

def test_one():  # unit test that writes to STDOUT
    print("WHOOPEE")
    assert(1)

def test_two(common_fixture):   # unit test that uses fixture from conftest.py
    assert(common_fixture == "DATA")

if __name__ == '__main__':
    pytest.main([__file__, "-s"])   # run tests (without stdout/stderr capture) when this script is run

