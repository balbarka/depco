"""
test_maker.py
~~~~~~~~~~~~~~~

This module contains unit tests for maker.

"""


def test_sum_a(maker):
    assert maker.sum_a() == 24


def test_sum_b(maker):
    assert maker.sum_b() == 21
