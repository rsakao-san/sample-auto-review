import pytest
from calculate_average import calculate_average


def test_calculate_average_normal():
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0


def test_calculate_average_empty():
    with pytest.raises(ValueError):
        calculate_average([])


def test_calculate_average_invalid_type():
    with pytest.raises(TypeError):
        calculate_average([1, "2", 3])


def test_calculate_average_float():
    assert calculate_average([1.5, 2.5]) == 2.0
