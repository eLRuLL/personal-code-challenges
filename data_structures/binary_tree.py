class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return repr(self.value)


class BinaryTree:
    def __init__(self):
        self.head = None

    def insert(self, value):
        if self.head:
            parent_node = None
            current_node = self.head
            left = True
            while current_node:
                parent_node = current_node
                if value < current_node.value:
                    current_node = current_node.left
                    left = True
                else:
                    current_node = current_node.right
                    left = False
            if left:
                parent_node.left = Node(value)
            else:
                parent_node.right = Node(value)
        else:
            self.head = Node(value)

    def find(self, value):
        parent_node = None
        current_node = self.head
        left = True
        while current_node:
            if value == current_node.value:
                return parent_node, current_node, left
            elif value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
                left = True
            else:
                parent_node = current_node
                current_node = current_node.right
                left = False

    def remove(self, value):
        parent_node, current_node, left = self.find(value)
        if current_node:
            if not current_node.left and not current_node.right:
                if left:
                    parent_node.left = None
                else:
                    parent_node.right = None
                del current_node
            elif current_node.left and not current_node.right:
                if left:
                    parent_node.left = current_node.left
                    del current_node
                else:
                    parent_node.right = current_node.left
                    del current_node
            elif not current_node.left and current_node.right:
                if left:
                    parent_node.left = current_node.right
                    del current_node
                else:
                    parent_node.right = current_node.right
            else:
                replace_parent = current_node
                replace_node = current_node.left
                replace_left = True
                while replace_node.right:
                    replace_parent = replace_node
                    replace_node = replace_node.right
                    replace_left = False
                current_node.value = replace_node.value
                if replace_left:
                    replace_parent.left = None
                else:
                    replace_parent.right = None
                del replace_node
