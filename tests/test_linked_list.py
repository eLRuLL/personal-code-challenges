import random

from data_structures.linked_list import LinkedList


def test_empty():
    ll = LinkedList()
    assert len(ll) == 0

    for _ in ll:
        assert False
    else:
        assert True


def test_works():
    ll = LinkedList()
    elements = [random.randrange(-1000000, 1000000) for _ in range(1000)]
    for elem in elements:
        ll.insert(elem)

    assert len(elements) == len(ll)

    while elements:
        elem_to_delete = elements.pop()
        assert bool(ll.find(elem_to_delete))
        ll.remove(elem_to_delete)
        assert len(elements) == len(ll)

    assert not elements
    assert ll.empty()


def test_removing_head():
    ll = LinkedList()

    ll.insert(1)
    ll.insert(2)
    ll.insert(3)

    ll.remove(1)
    assert len(ll) == 2
    assert ll.head.value == 2
    assert ll.head.next.value == 3
    assert not ll.head.next.next
    assert not ll.find(1)


def test_removing_tail():
    ll = LinkedList()

    ll.insert(1)
    ll.insert(2)
    ll.insert(3)

    ll.remove(3)
    assert len(ll) == 2
    assert ll.tail.value == 2
    assert not ll.tail.next
    assert not ll.head.next.next
    assert not ll.find(3)
