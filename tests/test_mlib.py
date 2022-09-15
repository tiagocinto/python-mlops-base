from mlib import scale_input, predict
import numpy as np
import pytest


@pytest.fixture
def test_array():
    val = np.random.randint(100, size=8)
    feature = val.reshape(-1, 1)
    return feature


def test_scale_input():
    assert scale_input(test_array()).shape == (1, 8)


def test_prediction(test_array):
    assert len(predict(test_array)) == 2
