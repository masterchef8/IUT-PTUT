__author__ = 'gaugendre'
import pytest

from algo_matrix import *


@pytest.fixture()
def matrix():
    return [[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1],
            [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]]


def test_out_of_zone(matrix):
    beginning = Pixel(0, 0)
    assert region_growing(matrix, beginning) is None


def test_in_zone(matrix):
    beginning = Pixel(1, 1)
    assert region_growing(matrix, beginning) == {Pixel(1, 0), Pixel(1, 1),
                                                 Pixel(1, 2), Pixel(2, 0),
                                                 Pixel(2, 1)}


def test_out_of_matrix(matrix):
    beginning = Pixel(15, 12)
    assert region_growing(matrix, beginning) is None