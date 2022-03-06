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


class Queue:
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

    # Add to the last so remove the first, first in first out
    def remove(self, idx=0):
        if self.head is None:
            return False
        else:
            self.head = self.head.next
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


b = Queue()
b.add(1)
b.add(2)
b.add(3)
b.remove()
b.print()
