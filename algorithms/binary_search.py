"""Only use with an ordered array"""


def binary_search(input_array, start, end, value):
    """
    :param input_array: list to search
    :param start: starting index
    :param end: ending index
    :param value: value to search
    :return: a tuple (found boolean, index)
    """
    if start != end:
        index = int((start+end)/2)
        if input_array[index] == value:
            return True, index
        elif value < input_array[index]:
            return binary_search(input_array, start, index, value)
        else:
            return binary_search(input_array, index+1, end, value)
    elif input_array[start] == value:
        return True, start
    else:
        return False, end
