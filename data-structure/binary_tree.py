class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            temp = self.root
            temp1 = temp
            while temp1 is not None:
                temp = temp1
                if data < temp1.data:
                    temp1 = temp1.left
                else:
                    temp1 = temp1.right
            if data < temp.data:
                temp.left = Node(data)
            else:
                temp.right = Node(data)

    # Left Node Right
    def inorder(self):
        lst = []
        self.inorder_1(self.root, lst)
        print(lst)

    def inorder_1(self, node, lst):
        if node is None:
            return []
        self.inorder_1(node.left, lst)
        lst.append(node.data)
        self.inorder_1(node.right, lst)

    # Node Left Right
    def preorder(self):
        lst = []
        self.preorder_1(self.root, lst)
        print(lst)

    def preorder_1(self, node, lst):
        if node is None:
            return []
        lst.append(node.data)
        self.preorder_1(node.left, lst)
        self.preorder_1(node.right, lst)

    # Left Right Node
    def postorder(self):
        lst = []
        self.postorder_1(self.root, lst)
        print(lst)

    def postorder_1(self, node, lst):
        if node is None:
            return []

        self.postorder_1(node.left, lst)
        self.postorder_1(node.right, lst)
        lst.append(node.data)


a = BinarySearchTree()
a.add(8)
a.add(4)
a.add(10)
a.add(9)
a.add(11)
a.add(3)
a.inorder()
a.postorder()
a.preorder()
