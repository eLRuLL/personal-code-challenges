from random import randint

from data_structures.max_stack import MaxStack


def test_stack_works():
    m = MaxStack()
    test_stack = []
    for _ in range(1000):
        x = randint(-500, 500)
        test_stack.append(x)
        m.push(x)

    for _ in range(1000):
        assert test_stack.pop() == m.pop()


def test_min_works():
    m = MaxStack()
    maximum = -1000
    for _ in range(1000):
        x = randint(-500, 500)
        maximum = max(maximum, x)
        m.push(x)

    assert m.maximum == maximum
