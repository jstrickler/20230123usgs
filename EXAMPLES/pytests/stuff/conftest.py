#!/usr/bin/env python
from pytest import fixture

@fixture
def common_fixture():  # user-defined fixture
    return "DATA"


def pytest_runtest_setup(item):  # predefined hook (all hooks start with __pytest__
    print("Hello from setup,", item)
