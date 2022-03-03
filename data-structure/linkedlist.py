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
a.print()