class MinHeap:
    def __init__(self):
        self._arr = []
        self.size = 0

    def minimum(self):
        if self._arr:
            return self._arr[0]

    def extract_minimum(self):
        root = self._arr[0]
        self._arr[0] = self._arr[-1]
        self._arr.pop()
        self.size -= 1
        current_index = 0
        while True:
            left_index = self._child_index(current_index)
            right_index = left_index + 1
            smallest_index = current_index
            if left_index < self.size and self._arr[left_index] < self._arr[current_index]:
                smallest_index = left_index
            if right_index < self.size and self._arr[right_index] < self._arr[smallest_index]:
                smallest_index = right_index
            if smallest_index != current_index:
                temp = self._arr[current_index]
                self._arr[current_index] = self._arr[smallest_index]
                self._arr[smallest_index] = temp
                current_index = smallest_index
            else:
                break
        return root

    def insert(self, value):
        self.size += 1
        self._arr.append(value)
        curr_index = self.size - 1
        while True:
            parent_index = self._parent_index(curr_index)
            if parent_index >= 0 and self._arr[parent_index] > value:
                temp = self._arr[parent_index]
                self._arr[parent_index] = value
                self._arr[curr_index] = temp
                curr_index = parent_index
            else:
                break

    def _parent_index(self, current_index):
        return int((current_index + 1)/2)-1

    def _child_index(self, current_index):
        return (current_index * 2) + 1
