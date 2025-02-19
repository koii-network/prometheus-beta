import pytest
from src.palindrome_linked_list import ListNode, is_palindromic_linked_list

def create_linked_list(values):
    """Helper function to create a linked list from a list of values"""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def test_empty_list():
    """Test an empty list is considered palindromic"""
    assert is_palindromic_linked_list(None) == True

def test_single_node_list():
    """Test a single node list is always palindromic"""
    head = ListNode(1)
    assert is_palindromic_linked_list(head) == True

def test_palindrome_even_length():
    """Test a palindromic list with even number of nodes"""
    head = create_linked_list([1, 2, 2, 1])
    assert is_palindromic_linked_list(head) == True

def test_palindrome_odd_length():
    """Test a palindromic list with odd number of nodes"""
    head = create_linked_list([1, 2, 3, 2, 1])
    assert is_palindromic_linked_list(head) == True

def test_non_palindrome_even_length():
    """Test a non-palindromic list with even number of nodes"""
    head = create_linked_list([1, 2, 3, 4])
    assert is_palindromic_linked_list(head) == False

def test_non_palindrome_odd_length():
    """Test a non-palindromic list with odd number of nodes"""
    head = create_linked_list([1, 2, 3, 4, 5])
    assert is_palindromic_linked_list(head) == False

def test_palindrome_with_different_values():
    """Test a palindromic list with different types of values"""
    head = create_linked_list(['a', 'b', 'b', 'a'])
    assert is_palindromic_linked_list(head) == True