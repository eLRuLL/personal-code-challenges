"""Numbers are randomly generated and stored into an (expanding) array. How would you keep track of the median?"""

from data_structures.min_heap import MinHeap
from data_structures.max_heap import MaxHeap
import random


def test_median_with_heaps():
    _list = [random.randint(0, 100) for _ in range(10)]

    min_heap = MinHeap()
    max_heap = MaxHeap()

    ordered_list = []

    for elem in _list:
        ordered_list.append(elem)
        ordered_list = sorted(ordered_list)
        print(elem)
        if max_heap.size and elem < max_heap.maximum():
            max_heap.insert(elem)
        else:
            min_heap.insert(elem)

        if min_heap.size-max_heap.size > 1:
            x = min_heap.extract_minimum()
            max_heap.insert(x)
        if max_heap.size-min_heap.size > 1:
            x = max_heap.extract_maximum()
            min_heap.insert(x)

        print(max_heap._arr)
        print(min_heap._arr)
        print(ordered_list)

        if len(ordered_list) % 2:
            median = ordered_list[int(len(ordered_list) / 2)]
            if min_heap.size > max_heap.size:
                assert median == min_heap.minimum()
            else:
                assert median == max_heap.maximum()
        else:
            median = (ordered_list[int(len(ordered_list) / 2)] + ordered_list[int((len(ordered_list) / 2)) - 1]) / 2
            assert median == (max_heap.maximum() + min_heap.minimum()) / 2
