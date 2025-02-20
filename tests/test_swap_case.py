import pytest
from src.swap_case import swap_case_string

def test_swap_case_mixed_case():
    """Test swapping case for a mixed case string"""
    assert swap_case_string("HeLLo WoRLd") == "hEllO wOrld"

def test_swap_case_all_lowercase():
    """Test swapping case for an all lowercase string"""
    assert swap_case_string("hello") == "HELLO"

def test_swap_case_all_uppercase():
    """Test swapping case for an all uppercase string"""
    assert swap_case_string("WORLD") == "world"

def test_swap_case_empty_string():
    """Test swapping case for an empty string"""
    assert swap_case_string("") == ""

def test_swap_case_with_numbers_and_symbols():
    """Test swapping case with numbers and symbols"""
    assert swap_case_string("Hello, World! 123") == "hELLO, wORLD! 123"