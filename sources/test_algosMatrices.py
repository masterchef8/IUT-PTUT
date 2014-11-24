__author__ = 'gaugendre'
import pytest
import numpy
from algos_matrices import *


@pytest.fixture()
def matrice():
    return [[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1],
            [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]]


@pytest.fixture()
def depart():
    return


def test_hors_zone(matrice):
    dep = Pixel(0, 0)
    assert croissance_region(matrice, dep) is None


def test_zone(matrice):
    dep = Pixel(1, 1)
    res = set()
    res.update({Pixel(1, 0), Pixel(1, 1), Pixel(1, 2), Pixel(2, 0), Pixel(2, 1)})
    function_call_result = croissance_region(matrice, dep)
    assert function_call_result.issubset(res)
    assert function_call_result.issuperset(res)


def test_hors_matrice(matrice):
    dep = Pixel(15, 12)
    assert croissance_region(matrice, dep) is None