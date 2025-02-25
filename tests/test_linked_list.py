import pytest
from src.linked_list import Node, LinkedList, create_linked_list

def test_node_creation():
    """Test Node class initialization."""
    node = Node(5)
    assert node.value == 5
    assert node.next is None

def test_linked_list_append():
    """Test appending nodes to a linked list."""
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    
    assert ll.to_list() == [1, 2, 3]

def test_create_linked_list():
    """Test creating a linked list with n nodes."""
    ll = create_linked_list(5)
    assert ll.to_list() == [1, 2, 3, 4, 5]

def test_create_linked_list_zero_nodes():
    """Test creating a linked list with zero nodes."""
    ll = create_linked_list(0)
    assert ll.to_list() == []

def test_create_linked_list_negative_nodes():
    """Test that creating a linked list with negative nodes raises an error."""
    with pytest.raises(ValueError):
        create_linked_list(-1)

def test_reverse_list_multiple_nodes():
    """Test reversing a linked list with multiple nodes."""
    ll = create_linked_list(5)
    ll.reverse_list()
    assert ll.to_list() == [5, 4, 3, 2, 1]

def test_reverse_list_single_node():
    """Test reversing a linked list with a single node."""
    ll = LinkedList()
    ll.append(1)
    ll.reverse_list()
    assert ll.to_list() == [1]

def test_reverse_list_empty():
    """Test reversing an empty list."""
    ll = LinkedList()
    ll.reverse_list()
    assert ll.to_list() == []

def test_to_list_method():
    """Test the to_list method conversion."""
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    
    assert ll.to_list() == [10, 20, 30]