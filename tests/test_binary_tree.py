import random
from data_structures.binary_tree import BinaryTree


def test_works():
    bt = BinaryTree()
    elements = [random.randrange(-1000000, 1000000) for _ in range(1000)]
    for elem in elements:
        bt.insert(elem)

    random.shuffle(elements)
    for elem in elements:
        print(bt.find(elem))
        bt.remove(elem)

    assert not bt.head
