import pytest
from src.linked_list_reversal import (
    Node, 
    create_linked_list, 
    append_node, 
    reverse_linked_list, 
    linked_list_to_list
)

def test_node_creation():
    """Test Node class initialization"""
    node = Node(5)
    assert node.value == 5
    assert node.next is None

def test_create_linked_list():
    """Test creating a linked list with n nodes"""
    # Test creating a list with 5 nodes
    head = create_linked_list(5)
    assert linked_list_to_list(head) == [1, 2, 3, 4, 5]
    
    # Test creating an empty list
    head = create_linked_list(0)
    assert head is None

def test_append_node():
    """Test appending nodes to a linked list"""
    # Append to an empty list
    head = append_node(None, 1)
    assert linked_list_to_list(head) == [1]
    
    # Append to an existing list
    head = create_linked_list(3)
    head = append_node(head, 4)
    assert linked_list_to_list(head) == [1, 2, 3, 4]

def test_reverse_linked_list():
    """Test reversing first n nodes of a linked list"""
    # Reverse first 3 nodes of a 5-node list
    head = create_linked_list(5)
    reversed_head = reverse_linked_list(head, 3)
    assert linked_list_to_list(reversed_head) == [3, 2, 1, 4, 5]
    
    # Reverse entire list
    head = create_linked_list(5)
    reversed_head = reverse_linked_list(head, 5)
    assert linked_list_to_list(reversed_head) == [5, 4, 3, 2, 1]
    
    # Reverse 0 or 1 node (should return original list)
    head = create_linked_list(5)
    assert linked_list_to_list(reverse_linked_list(head, 0)) == [1, 2, 3, 4, 5]
    
    head = create_linked_list(5)
    assert linked_list_to_list(reverse_linked_list(head, 1)) == [1, 2, 3, 4, 5]

def test_reverse_empty_list():
    """Test reversing an empty list"""
    assert reverse_linked_list(None, 3) is None