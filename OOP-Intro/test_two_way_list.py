from two_way_list import *
#traverce_list is used in every test so there is no need to test it

def test_insert_in_empty():
    linked_list = DoublyLinkedList()
    linked_list.insert_in_emptylist(50)
    assert linked_list.traverse_list() == [50]

def test_insert_at_start():
    linked_list = DoublyLinkedList()
    linked_list.insert_in_emptylist(50)
    linked_list.insert_at_start(10)
    assert linked_list.traverse_list() == [10, 50]

def test_insert_after_item():
    linked_list = DoublyLinkedList()
    assert linked_list.insert_after_item(5, 10) == None
    linked_list.insert_in_emptylist(50)
    linked_list.insert_at_start(10)
    linked_list.insert_after_item(10,5)
    assert linked_list.traverse_list() == [10, 5, 50]

def test_insert_at_end():
    linked_list = DoublyLinkedList()
    linked_list.insert_in_emptylist(50)
    linked_list.insert_at_start(10)
    linked_list.insert_at_end(15)
    assert linked_list.traverse_list() == [10, 50, 15]

def test_reverse_linked_list():
    linked_list = DoublyLinkedList()
    assert linked_list.reverse_linked_list() == None
    linked_list.insert_in_emptylist(50)
    linked_list.insert_at_start(10)
    linked_list.insert_at_end(15)
    linked_list.reverse_linked_list()
    assert linked_list.traverse_list() == [15, 50, 10]

def test_delete_element_by_value():
    linked_list = DoublyLinkedList()
    assert linked_list.delete_element_by_value(5) == None
    linked_list.insert_in_emptylist(50)
    linked_list.insert_at_start(10)
    linked_list.insert_at_end(15)
    linked_list.delete_element_by_value(50)
    assert linked_list.traverse_list() == [10, 15]

def test_delete_at_end():
    linked_list = DoublyLinkedList()
    assert linked_list.delete_at_end() == None
    linked_list.insert_in_emptylist(50)
    linked_list.insert_at_start(10)
    linked_list.insert_at_end(15)
    linked_list.delete_at_end()
    assert linked_list.traverse_list() == [10, 50]

def test_delete_at_start():
    linked_list = DoublyLinkedList()
    assert linked_list.delete_at_start() == None
    linked_list.insert_in_emptylist(50)
    linked_list.insert_at_start(10)
    linked_list.insert_at_end(15)
    linked_list.delete_at_start()
    assert linked_list.traverse_list() == [50, 15]
