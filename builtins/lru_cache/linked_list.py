class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def __repr__(self):
        return f"<Node key: {self.key}, value: {self.value}>"


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def __len__(self):
        return self.size

    def append(self, node: Node):
        prev_node = self.tail.prev
        prev_node.next = node

        node.prev = prev_node
        node.next = self.tail

        self.tail.prev = node

        self.size += 1

    def remove(self, node: Node):
        prev_node = node.prev
        next_node = node.next

        node.prev = None
        node.next = None

        prev_node.next = next_node
        next_node.prev = prev_node

        self.size -= 1

    def popleft(self):
        if self.size == 0:
            return None
        node = self.head.next
        self.remove(node)
        return node