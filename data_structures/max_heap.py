class MaxHeap:
    def __init__(self):
        self._arr = []
        self.size = 0

    def maximum(self):
        return self._arr[0]

    def insert(self, value):
        self._arr.append(value)
        current_index = self.size
        self.size += 1
        while True:
            parent_index = self._parent_index(current_index)
            if parent_index >= 0 and self._arr[parent_index] < value:
                temp = self._arr[parent_index]
                self._arr[parent_index] = value
                self._arr[current_index] = temp
                current_index = parent_index
            else:
                break

    def extract_maximum(self):
        root = self._arr[0]
        self.size -= 1
        self._arr[0] = self._arr[-1]
        self._arr.pop()
        current_index = 0
        while True:
            left_index = self._child_index(current_index)
            right_index = left_index + 1
            maximum_index = current_index
            if left_index < self.size and self._arr[left_index] > self._arr[current_index]:
                maximum_index = left_index
            if right_index < self.size and self._arr[right_index] > maximum_index:
                maximum_index = right_index
            if maximum_index != current_index:
                temp = self._arr[maximum_index]
                self._arr[maximum_index] = self._arr[current_index]
                self._arr[current_index] = temp
                current_index = maximum_index
            else:
                break
        return root

    def _parent_index(self, current_index):
        return int((current_index + 1)/2) - 1

    def _child_index(self, current_index):
        return (current_index * 2) + 1
