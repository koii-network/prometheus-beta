import pytest
from src.linked_list import ListNode, reverse_linked_list

def list_to_array(head):
    """
    Convert a linked list to an array for easy comparison.
    
    Args:
        head (ListNode): Head of the linked list.
    
    Returns:
        list: Array representation of the linked list values.
    """
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def array_to_list(arr):
    """
    Convert an array to a linked list.
    
    Args:
        arr (list): Input array of values.
    
    Returns:
        ListNode: Head of the created linked list.
    """
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def test_reverse_empty_list():
    """Test reversing an empty list."""
    assert reverse_linked_list(None) is None

def test_reverse_single_node_list():
    """Test reversing a list with a single node."""
    single_node = ListNode(1)
    reversed_list = reverse_linked_list(single_node)
    assert list_to_array(reversed_list) == [1]

def test_reverse_multiple_nodes_list():
    """Test reversing a list with multiple nodes."""
    # Create original list: 1 -> 2 -> 3 -> 4 -> 5
    original_list = array_to_list([1, 2, 3, 4, 5])
    
    # Reverse the list
    reversed_list = reverse_linked_list(original_list)
    
    # Check if reversed correctly: 5 -> 4 -> 3 -> 2 -> 1
    assert list_to_array(reversed_list) == [5, 4, 3, 2, 1]

def test_reverse_two_node_list():
    """Test reversing a list with two nodes."""
    original_list = array_to_list([1, 2])
    reversed_list = reverse_linked_list(original_list)
    assert list_to_array(reversed_list) == [2, 1]

def test_repeated_reversal():
    """Test that reversing twice returns to the original order."""
    original_list = array_to_list([1, 2, 3, 4, 5])
    
    # First reversal
    first_reversal = reverse_linked_list(original_list)
    assert list_to_array(first_reversal) == [5, 4, 3, 2, 1]
    
    # Second reversal
    second_reversal = reverse_linked_list(first_reversal)
    assert list_to_array(second_reversal) == [1, 2, 3, 4, 5]