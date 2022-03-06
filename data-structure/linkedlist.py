"""
A linked list is a dynamic data structure. The number of nodes in a list is not fixed and can
grow and shrink on demand. Any application which has to deal with an unknown number of objects will
need to use a linked list. ll is a very common data structure that is used to create other data structures like
trees, graphs, hashing. etc.
"""


class Node:
    def __init__(self):
        self.value = None
        self.next = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next


class SLL:
    def __init__(self):
        self.head = None
        self.length = 0

    def add(self, value):
        if self.head is None:
            self.head = Node()
            self.head.set_value(value)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = Node()
            temp.next.set_value(value)
        self.length += 1

    # Remove at position idx if a list [1, 2, 3, 4] - idx = 1 will get value 1
    def remove(self, idx):
        if idx > self.length or idx <= 0:
            return False
        # Remove first element
        elif idx == 1:
            self.head = self.head.next
        # Remove last element
        elif idx == self.length:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
        # Remove inside
        else:
            idx -= 2
            temp = self.head
            while idx != 0:
                idx -= 1
                temp = temp.next
            temp1 = temp.next.next
            temp.next = temp1
        self.length -= 1
        return True

    def print(self):
        temp = self.head
        lst = []
        while temp is not None:
            lst.append(temp.value)
            temp = temp.next
        print(lst)


a = SLL()
a.add(1)
a.add(2)
a.add(3)
a.add(4)
a.add(5)
a.remove(4)
a.print()
