"""
A stack abstract type is a container of objects that arc inserted and removed according
to the last-in first-out (LIFO) principle.
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


class Stack:
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

    # Add to the last so remove the last, last in first out
    def remove(self, idx=0):
        if self.head is None:
            return False
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
        self.length -= 1
        return True

    def print(self):
        temp = self.head
        lst = []
        while temp is not None:
            lst.append(temp.value)
            temp = temp.next
        print(lst)
        return


b = Stack()
b.add(1)
b.add(2)
b.add(3)
b.remove()
b.print()
