from random import randint

from data_structures.min_stack import MinStack


def test_stack_works():
    m = MinStack()
    test_stack = []
    for _ in range(1000):
        x = randint(-500, 500)
        test_stack.append(x)
        m.push(x)

    for _ in range(1000):
        assert test_stack.pop() == m.pop()


def test_min_works():
    m = MinStack()
    minimum = 1000
    for _ in range(1000):
        x = randint(-500, 500)
        minimum = min(minimum, x)
        m.push(x)

    assert m.minimum == minimum
