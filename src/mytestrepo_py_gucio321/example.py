def sum(a : [int, float], b : [int, float] = 0) -> [int, float]:
    """
    sum returns a sum of 2 integer numbers.

    :param a: first number
    :param b: second number, default is 0
    :return: sum of a and b
    """
    assert isinstance(a, (int, float)), "a must be an integer or a float"
    assert isinstance(b, (int, float)), "a must be an integer or a float"
    return a + b
