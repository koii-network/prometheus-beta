import pytest
from src.linked_list_reversal import create_linked_list, LinkedList, Node


def test_node_creation():
    """Test basic Node creation"""
    node = Node(5)
    assert node.value == 5
    assert node.next is None


def test_linked_list_creation():
    """Test creating a linked list with multiple nodes"""
    ll = create_linked_list(5)
    assert ll.to_list() == [1, 2, 3, 4, 5]


def test_empty_list_creation():
    """Test creating an empty list"""
    ll = create_linked_list(0)
    assert ll.to_list() == []


def test_create_linked_list_negative():
    """Test creating a list with negative nodes raises an error"""
    with pytest.raises(ValueError, match="Number of nodes cannot be negative"):
        create_linked_list(-1)


def test_reverse_entire_list():
    """Test reversing an entire list"""
    ll = create_linked_list(5)
    ll.reverse()
    assert ll.to_list() == [5, 4, 3, 2, 1]


def test_reverse_partial_list():
    """Test reversing a specific number of nodes"""
    ll = create_linked_list(5)
    ll.reverse(3)
    assert ll.to_list() == [3, 2, 1, 4, 5]


def test_reverse_entire_single_node_list():
    """Test reversing a single-node list"""
    ll = create_linked_list(1)
    ll.reverse()
    assert ll.to_list() == [1]


def test_reverse_empty_list():
    """Test reversing an empty list"""
    ll = LinkedList()
    ll.reverse()
    assert ll.to_list() == []


def test_reverse_partial_with_invalid_n():
    """Test reversing with invalid n raises an error"""
    ll = create_linked_list(5)
    
    # Negative n
    with pytest.raises(ValueError, match="Number of nodes to reverse cannot be negative"):
        ll.reverse(-1)
    
    # n greater than list length
    with pytest.raises(ValueError, match="Cannot reverse 6 nodes in a list with 5 nodes"):
        ll.reverse(6)


def test_reverse_with_different_partial_lengths():
    """Test reversing lists with different partial lengths"""
    # Test reversing first 2 nodes
    ll = create_linked_list(5)
    ll.reverse(2)
    assert ll.to_list() == [2, 1, 3, 4, 5]
    
    # Reset and test reversing 4 nodes
    ll = create_linked_list(5)
    ll.reverse(4)
    assert ll.to_list() == [4, 3, 2, 1, 5]