class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self._length = 0

        # iteration
        self.current_node = None

    def __len__(self):
        return self._length

    def __iter__(self):
        self.current_node = self.head
        return self

    def __next__(self):
        if not self.current_node:
            raise StopIteration
        else:
            return_node = self.current_node
            self.current_node = self.current_node.next
            return return_node

    def empty(self):
        return not bool(self._length)

    def insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._length += 1

    def find(self, value):
        prev_node = None
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return prev_node, current_node
            else:
                prev_node = current_node
                current_node = current_node.next

    def remove(self, value):
        prev_node, current_node = self.find(value)
        if current_node:
            if prev_node:
                if not current_node.next:
                    # removing tail
                    self.tail = prev_node
                prev_node.next = current_node.next
            else:
                # removing head
                self.head = current_node.next
            del current_node
            self._length -= 1
            return True
        return False
