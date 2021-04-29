# DONE: Binary Trees
# https://www.geeksforgeeks.org/binarytree-module-in-python/
# https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm


# tree = MyBinTree(8) => [None, 8, None] 
# tree.add(2) => [[None, 2, None], 8, None]
# tree.add(4) => [[[None, 2, None], 4, [None]], 8, None]
# tree.add(5) => [[[None, 2, None], 4, [None, 5, None]], 8, None]

class MyBinTree:

    list_return = []

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
        # this is iteration using recursion
        # we want to get the right-most item and print it first.
        
        
        # tree.add(2) => [[None, 2, None], 8, None]
        # Why [2, 8] and not [8, 2]?

        if self.right:
            self.right.print_tree()
        self.list_return.append(self.value)
        #print(self.value)
        if self.left:
            self.left.print_tree()
        return self.list_return

    # filter, map, reduce
    # Filter: filter(pred_func, iterable)

# DOESNT WORK
    # def sum_even(self):
    #     return sum(
    #         filter(
    #             lambda x: x % 2 == 0, # predicate
    #             self.print_tree() # iterable
    #         )
    #     )

# Да се напише програма, която намира сумата на четните стойности от върховете на дадено двоично дърво.
    def inorderTraversal(self, item):
        res = []
        if item:
            res = self.inorderTraversal(item.left)
            res.append(item.value)
            res = res + self.inorderTraversal(item.right)
        return res

    def sum_even(self):
        even_amount = 0
        list_from_tree = self.inorderTraversal(self)
        for i in list_from_tree:
            if i % 2 == 0:
                even_amount += 1
        #print(even_amount)
        return even_amount