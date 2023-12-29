class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None
        self.prev_node = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next_node
        print()

    def replace_odd_positions(self):
        current = self.head
        while current:
            if current.data % 2 == 1:
                current.data = 0
            current = current.next_node


linked_list = DoublyLinkedList()

for i in range(1, 21):
    linked_list.append(i)

linked_list.display()

linked_list.replace_odd_positions()

linked_list.display()
