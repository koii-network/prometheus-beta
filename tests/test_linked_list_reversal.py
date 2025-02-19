import pytest
from src.linked_list_reversal import ListNode, reverse_linked_list

def list_to_array(head):
    """Convert linked list to array for easy comparison"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def array_to_list(arr):
    """Convert array to linked list"""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def test_reverse_linked_list_normal():
    """Test reversing a normal linked list"""
    input_list = array_to_list([1, 2, 3, 4, 5])
    reversed_list = reverse_linked_list(input_list)
    assert list_to_array(reversed_list) == [5, 4, 3, 2, 1]

def test_reverse_linked_list_single_node():
    """Test reversing a single-node list"""
    input_list = array_to_list([42])
    reversed_list = reverse_linked_list(input_list)
    assert list_to_array(reversed_list) == [42]

def test_reverse_linked_list_empty():
    """Test reversing an empty list"""
    input_list = None
    reversed_list = reverse_linked_list(input_list)
    assert reversed_list is None

def test_reverse_linked_list_two_nodes():
    """Test reversing a two-node list"""
    input_list = array_to_list([1, 2])
    reversed_list = reverse_linked_list(input_list)
    assert list_to_array(reversed_list) == [2, 1]

def test_reverse_linked_list_preserved_node_links():
    """Ensure node links are correctly preserved during reversal"""
    input_list = array_to_list([1, 2, 3, 4, 5])
    reversed_list = reverse_linked_list(input_list)
    
    # Check that the last node points to None
    current = reversed_list
    while current.next:
        current = current.next
    assert current.next is None