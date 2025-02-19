import pytest
from src.linked_list_palindrome import ListNode, is_palindrome_linked_list

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

def test_palindrome_even_length():
    # Palindrome with even length: 1 -> 2 -> 2 -> 1
    head = create_linked_list([1, 2, 2, 1])
    assert is_palindrome_linked_list(head) == True

def test_palindrome_odd_length():
    # Palindrome with odd length: 1 -> 2 -> 3 -> 2 -> 1
    head = create_linked_list([1, 2, 3, 2, 1])
    assert is_palindrome_linked_list(head) == True

def test_non_palindrome():
    # Non-palindrome list: 1 -> 2 -> 3 -> 4
    head = create_linked_list([1, 2, 3, 4])
    assert is_palindrome_linked_list(head) == False

def test_single_element():
    # Single element list should be a palindrome
    head = create_linked_list([1])
    assert is_palindrome_linked_list(head) == True

def test_empty_list():
    # Empty list should be considered a palindrome
    head = create_linked_list([])
    assert is_palindrome_linked_list(head) == True

def test_two_element_palindrome():
    # Two-element palindrome: 2 -> 2
    head = create_linked_list([2, 2])
    assert is_palindrome_linked_list(head) == True

def test_two_element_non_palindrome():
    # Two-element non-palindrome: 1 -> 2
    head = create_linked_list([1, 2])
    assert is_palindrome_linked_list(head) == False