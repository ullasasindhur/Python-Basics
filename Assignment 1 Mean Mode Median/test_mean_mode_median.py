import mean_mode_median
import pytest


@pytest.mark.parametrize("list,value", [
    ([0, 0, 0, 10, 15, 20], 7.5),
    ([-10, -150, -90, 10, 15, 20], -34.166666666666664),
    ([0], 0),
    (['a', 'b', 0], "Invalid Data")
])
def test_sampleMean(list, value):
    assert mean_mode_median.sampleMean(list) == value


def test_error_sameplMean():
    pytest.raises(ZeroDivisionError, mean_mode_median.sampleMean, [])


@pytest.fixture
def zero_list():
    return [0]


@pytest.fixture
def non_empty_list():
    return [9, 10, 98, 129, 30, 56, 78, 98, 32]


@pytest.fixture
def append_list(non_empty_list):
    non_empty_list.append(58)
    return non_empty_list


def test_sampleMedian_zero_list(zero_list):
    assert mean_mode_median.sampleMedian(zero_list) == 0


def test_sampleMedian_non_empty_list(non_empty_list):
    assert mean_mode_median.sampleMedian(non_empty_list) == 56


def test_sampleMedian_append_list(append_list):
    assert mean_mode_median.sampleMedian(append_list) == 57.0


def test_sampleMode_append_list(append_list):
    assert mean_mode_median.sampleMode(append_list) == 98


@pytest.mark.parametrize("input,output", [
    ([1, 1, 1, 1, 1, 1], 1),
    ([0, 0, 0, 1, 1, 1, 2, 3, 5, 6], 0),
    ([11, 627, 83, 94, 45, 1, 987], 1)
])
def test_sampleMode(input, output):
    assert mean_mode_median.sampleMode(input) == output
