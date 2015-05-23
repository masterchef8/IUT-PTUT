# -*- coding: utf-8 -*- 

__author__ = 'gaugendre'
import pytest

from algo_matrix import *


@pytest.fixture()
def matrix():
    return [[72, 72, 72, 72, 72, 72, 72, 24, 24, 11, 11, 72, 72, 11, 1],
            [15, 15, 15, 72, 72, 72, 72, 36, 36, 36, 72, 72, 72, 36, 1],
            [36, 8, 72, 72, 72, 72, 72, 72, 24, 72, 72, 72, 72, 72, 1],
            [72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 65],
            [24, 24, 24, 8, 8, 8, 8, 25, 24, 24, 24, 24, 24, 25, 1],
            [72, 72, 72, 72, 72, 25, 72, 72, 72, 25, 72, 72, 72, 72, 85],
            [25, 24, 24, 24, 72, 24, 72, 72, 25, 25, 25, 72, 72, 72, 94],
            [72, 72, 72, 25, 24, 24, 24, 11, 11, 72, 72, 72, 72, 72, 155]]


@pytest.fixture()
def seuil():
    return 50


def test_out_of_zone(matrix, seuil):
    beginning = Pixel(0, 0)
    assert region_growing(matrix, beginning, seuil) is None


def test_in_zone(matrix, seuil):
    beginning = Pixel(1, 1)
    assert region_growing(matrix, beginning, seuil) == {Pixel(1, 0), Pixel(1, 1),
                                                        Pixel(1, 2), Pixel(2, 0),
                                                        Pixel(2, 1)}


def test_out_of_matrix(matrix, seuil):
    beginning = Pixel(15, 12)
    assert region_growing(matrix, beginning, seuil) is None

def test_average_color(seuil):
    avg = lakeAverageColor("img/test1.png", Pixel(214, 142), seuil)
    assert avg.vert == 214
    assert avg.hor == 142
    assert avg.red == 0
    assert avg.green == 138
    assert avg.blue == 167
    assert avg.alpha == 0
