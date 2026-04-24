from .example import *
import pytest

def test_sum():
    test_cases = [
            {
                "Name": "two positive integers",
                "A": 2,
                "B": 3,
                "expected": 5
            },
            {
                "Name": "Positive and negative integer",
                "A": 5,
                "B": -2,
                "expected": 3,
            },
            {
                "Name": "two floats",
                "A": 3.14,
                "B": 2.71,
                "expected": 5.85,
            },
            {
                "Name": "float and an integer",
                "A": 2.5,
                "B": 2,
                "expected": 4.5,
            },
            {
                "Name": "integer and float",
                "A": 2,
                "B": 2.5,
                "expected": 4.5,
            }
    ]

    for tc in test_cases:
        assert sum(tc["A"], tc["B"]) == tc["expected"], f"Failed {tc['Name']}"


def test_sum_exceptions():
    """
    check if VlueError is raised when trying to sum string with an integer
    """
    with pytest.raises(TypeError):
        sum("something", 5)
