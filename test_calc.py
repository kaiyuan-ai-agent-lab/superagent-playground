from calc import add, multiply, divide


def test_add():
    assert add(2, 3) == 5


def test_multiply():
    assert multiply(2, 3) == 6


def test_divide():
    assert divide(6, 3) == 2
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    try:
        divide(5, 0)
        assert False, "Expected ZeroDivisionError"
    except ZeroDivisionError:
        pass
