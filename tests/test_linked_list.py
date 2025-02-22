import pytest
from src.linked_list import LinkedList

def test_linked_list_creation():
    """
    Test creating a linked list with a specified number of nodes.
    """
    ll = LinkedList()
    ll.create_list(5)
    assert ll.to_list() == [0, 1, 2, 3, 4]

def test_linked_list_reverse():
    """
    Test reversing a linked list.
    """
    ll = LinkedList()
    ll.create_list(5)
    ll.reverse()
    assert ll.to_list() == [4, 3, 2, 1, 0]

def test_reverse_empty_list():
    """
    Test reversing an empty list.
    """
    ll = LinkedList()
    ll.reverse()
    assert ll.to_list() == []

def test_reverse_single_node_list():
    """
    Test reversing a list with a single node.
    """
    ll = LinkedList()
    ll.append(42)
    ll.reverse()
    assert ll.to_list() == [42]

def test_append_method():
    """
    Test appending nodes to the linked list.
    """
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    assert ll.to_list() == [10, 20, 30]