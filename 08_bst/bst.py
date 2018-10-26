class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.visited = 0

    def insert(self, value):
        self.add_item(self.root, value)

    def fromArray(self, array):
        for value in array:
            self.insert(value)

    def search(self, value):
        self.visited = 0
        if not self.root:
            return False
        return self.search_node(self.root, value)

    def min(self):
        if not self.root:
            return None

        self.visited = 1
        node = self.root
        while node.left:
            self.visited += 1
            node = node.left

        return node.value

    def max(self):
        if not self.root:
            return None

        self.visited = 1
        node = self.root
        while node.right:
            self.visited += 1
            node = node.right

        return node.value

    def visitedNodes(self):
        return self.visited

    def add_item(self, parent, value):
        """
        :type parent: Node
        :param value
        """
        if not parent:
            self.root = Node(value)
            return

        if value == parent.value:
            return

        if value > parent.value:
            if not parent.right:
                parent.right = Node(value)
            else:
                self.add_item(parent.right, value)
        else:
            if not parent.left:
                parent.left = Node(value)
            else:
                self.add_item(parent.left, value)

    def search_node(self, parent, value):
        """
        :type parent: Node
        :param value
        """
        self.visited += 1

        if parent.value == value:
            return True
        if parent.right and value > parent.value:
            return self.search_node(parent.right, value)
        if parent.left and value < parent.value:
            return self.search_node(parent.left, value)
        return False
