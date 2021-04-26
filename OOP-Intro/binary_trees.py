# DONE: Binary Trees
# https://www.geeksforgeeks.org/binarytree-module-in-python/
# https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm

global list_return
list_return = []

class MyBinTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def add(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = MyBinTree(value)
                else:
                    self.left.add(value)
            elif value > self.value:
                if self.right is None:
                    self.right = MyBinTree(value)
                else:
                    self.right.add(value)
        else:
            self.value = value

    def print_tree(self):
        # програма, която извежда всички положителни,
        # а след това и всички отрицателни стойности от върховете на дадено двоично дърво

        # calls print_tree of the current objs "left" obj
        # this is iteration using recursion 😮
        # we want to get the right-most item and print it first.
        if self.right:
            self.right.print_tree()
        list_return.append(self.value)
        #print(self.value)
        if self.left:
            self.left.print_tree()
        return list_return

# Да се напише програма, която намира сумата на четните стойности от върховете на дадено двоично дърво.
    def inorderTraversal(self, item):
        res = []
        if item:
            res = self.inorderTraversal(item.left)
            res.append(item.value)
            res = res + self.inorderTraversal(item.right)
        return res

    def check_even(self):
        even_amount = 0
        list_from_tree = self.inorderTraversal(self)
        for i in list_from_tree:
            if i % 2 == 0:
                even_amount += 1
        #print(even_amount)
        return even_amount