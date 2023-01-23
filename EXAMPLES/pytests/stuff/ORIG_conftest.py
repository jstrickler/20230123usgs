#!/usr/bin/env python
from pytest import fixture

@fixture
def common_fixture():  # <1>
    return "DATA"


def pytest_runtest_setup(item):  # <2>
    print("Hello from setup,", item)
