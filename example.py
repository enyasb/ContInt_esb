def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5


def subtract(a, b):
    return -b + a

def test_subtract():
    assert subtract(3, 2) == 1
