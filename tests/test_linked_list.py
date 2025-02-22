import pytest
from src.linked_list import ListNode, reverse_linked_list, list_to_array, array_to_linked_list

def test_reverse_empty_list():
    """Test reversing an empty list"""
    assert reverse_linked_list(None) is None

def test_reverse_single_node_list():
    """Test reversing a list with a single node"""
    head = ListNode(5)
    result = reverse_linked_list(head)
    assert result.val == 5
    assert result.next is None

def test_reverse_multiple_node_list():
    """Test reversing a list with multiple nodes"""
    # Create list: 1 -> 2 -> 3 -> 4 -> 5
    head = array_to_linked_list([1, 2, 3, 4, 5])
    
    # Reverse the list
    reversed_head = reverse_linked_list(head)
    
    # Convert back to array to verify
    result = list_to_array(reversed_head)
    assert result == [5, 4, 3, 2, 1]

def test_reverse_two_node_list():
    """Test reversing a list with two nodes"""
    head = array_to_linked_list([1, 2])
    reversed_head = reverse_linked_list(head)
    result = list_to_array(reversed_head)
    assert result == [2, 1]

def test_multiple_reversal():
    """Test that multiple reversals work correctly"""
    head = array_to_linked_list([1, 2, 3])
    
    # First reversal
    reversed_head = reverse_linked_list(head)
    result1 = list_to_array(reversed_head)
    assert result1 == [3, 2, 1]
    
    # Second reversal
    re_reversed_head = reverse_linked_list(reversed_head)
    result2 = list_to_array(re_reversed_head)
    assert result2 == [1, 2, 3]