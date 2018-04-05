"""Given two sorted arrays, find the number of elements in common.
The arrays are the same length and each has all distinct elements."""
from algorithms.binary_search import binary_search


def test_find_common_elements():
    list1 = [13, 27, 35, 40, 49, 55, 59]
    list2 = [17, 35, 39, 40, 55, 58, 60]

    min_index1 = None
    min_index2 = None
    starting_index = 0
    for index, elem in enumerate(list1):
        min_index2 = binary_search(list2, starting_index, len(list2)-1, elem)
        if min_index2[0]:
            min_index2 = min_index2[1]
            min_index1 = index
            break
        starting_index = min_index2[1]

    if min_index1 is not None:
        result = [list1[min_index1]]
        min_index1 += 1
        min_index2 += 1
        while min_index1 < len(list1) and min_index2 < len(list2):
            if list1[min_index1] == list2[min_index2]:
                result.append(list1[min_index1])
                min_index1 += 1
                min_index2 += 1
            elif list1[min_index1] > list2[min_index2]:
                min_index2 += 1
            else:
                min_index1 += 1

        assert sorted(list(set(list1) & set(list2))) == result
