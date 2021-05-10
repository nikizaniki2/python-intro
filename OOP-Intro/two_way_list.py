# DONE?: Свързан линеен списък
# The code is pasted but I've gone through it in order to understand it.
# https://stackabuse.com/doubly-linked-list-with-python-examples/

class Node:
    # Всеки елемент е инстанция на клас
    def __init__(self, data):
        # Item stores the list item value.
        self.item = data
        # nref stores the position to the next item in the list (kind of like pointers in c/cpp)
        self.nref = None
        # pref stores the position to the previous item in the list (if there is one)
        self.pref = None

class DoublyLinkedList:
    def __init__(self):
        self.start_node = None
        # start_node is None in order for us to easily detect an empty list
    
    # Да се реализират основните операции за работа с двусвързан линеен списък.

    def insert_in_emptylist(self, data):
        #check if list is truly empty and create the first item or display an error message 
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("list is not empty")

    def insert_at_start(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            print("node inserted")
            return
        new_node = Node(data)
        #we set the new first items next item pointer to the old first values position
        new_node.nref = self.start_node
        #the old first item now has a pref pointer value to the new first item
        self.start_node.pref = new_node
        #replace the value of start_node with the new first items value
        self.start_node = new_node
    
    def insert_at_end(self, data):
        #if the list is empty a new item will become the last
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        #while the next item is not None (ie: we have reached the last position) get the next item location and go there
        while n.nref is not None:
            n = n.nref
        #now that we are the last item we can just change the nref pointer of the old last item from None to our new node
        new_node = Node(data)
        n.nref = new_node
        #also don't forget to point to the old item so that we still have a two-way list
        new_node.pref = n

    def insert_after_item(self, x, data):
        #x is the value by which to search
        #data is the value which to insert after x
        #if the list is empty we cannot "insert after item"
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            #while the next item is not None (ie: we have reached the last position) get the next item
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            #if we reach the end and n is not in x we error out
            if n is None:
                print("item not in the list")
            else:
            #in case n is in x we do the same switcher-o we aways do
                new_node = Node(data)
                new_node.pref = n
                new_node.nref = n.nref
                if n.nref is not None:
                    n.nref.prev = new_node
                n.nref = new_node
    
    def traverse_list(self):
        #on empty error
        if self.start_node is None:
            print("List has no element")
            return False
        else:
            #we loop for n in the list of items until we reach the last item
            n = self.start_node
            final_list = []
            while n is not None:
                final_list.append(n.item)
                print(n.item , " ")
                n = n.nref
            return final_list

    def reverse_linked_list(self):
        #again on empty error out
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        #save the first item in a temp var (p)
        p = self.start_node
        #save the next item in a temp var (q)
        q = p.nref
        #next item pointer is set to None because we will place p in last place
        p.nref = None
        #the first item is now ordered after the second one (they switch places)
        p.pref = q
        while q is not None:
            #switchar-o
            q.pref = q.nref
            q.nref = p
            p = q
            q = q.pref
        self.start_node = p

    def delete_element_by_value(self, x):
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        #in case the list only has 1 element
        if self.start_node.nref is None:
            #if the first element matches
            if self.start_node.item == x:
                #remove it
                self.start_node = None
            else:
                print("Item not found")
            return 
        #if the item matches fix the pointers and remove (first item only) (delete_at_start())
        if self.start_node.item == x:
            self.start_node = self.start_node.nref
            self.start_node.pref = None
            return
        #start looping over the list
        n = self.start_node
        while n.nref is not None:
            #if we have a match stop looping and fix pointers
            if n.item == x:
                break
            n = n.nref
        if n.nref is not None:
            n.pref.nref = n.nref
            n.nref.pref = n.pref
        else:
            if n.item == x:
                n.pref.nref = None
            else:
                print("Element not found")

    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        #in case we only have one item in the list 
        if self.start_node.nref is None:
            self.start_node = None
            return
        #else just fix the pointers
        self.start_node = self.start_node.nref
        self.start_prev = None

    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        #in case we only have one item in the list 
        if self.start_node.nref is None:
            self.start_node = None
            return
        #loop until you get to the last item
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        #remove the pointer to next item (from the previous item)
        n.pref.nref = None
