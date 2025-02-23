import pytest
from src.linked_list import ListNode, reverse_linked_list

def list_to_array(head):
    """Convert a linked list to an array for easy comparison."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def array_to_list(arr):
    """Convert an array to a linked list."""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def test_empty_list():
    """Test reversing an empty list."""
    assert reverse_linked_list(None) is None

def test_single_node_list():
    """Test reversing a list with a single node."""
    single_node = ListNode(5)
    reversed_list = reverse_linked_list(single_node)
    assert list_to_array(reversed_list) == [5]

def test_multiple_nodes_list():
    """Test reversing a list with multiple nodes."""
    input_arr = [1, 2, 3, 4, 5]
    input_list = array_to_list(input_arr)
    reversed_list = reverse_linked_list(input_list)
    assert list_to_array(reversed_list) == list(reversed(input_arr))

def test_two_node_list():
    """Test reversing a list with two nodes."""
    input_arr = [1, 2]
    input_list = array_to_list(input_arr)
    reversed_list = reverse_linked_list(input_list)
    assert list_to_array(reversed_list) == list(reversed(input_arr))

def test_large_list():
    """Test reversing a larger list."""
    input_arr = list(range(1, 101))  # 1 to 100
    input_list = array_to_list(input_arr)
    reversed_list = reverse_linked_list(input_list)
    assert list_to_array(reversed_list) == list(reversed(input_arr))