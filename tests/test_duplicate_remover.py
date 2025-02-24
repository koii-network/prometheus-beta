import pytest
from src.duplicate_remover import deleteDuplicates

def test_delete_duplicates_basic():
    """Test basic functionality of removing duplicates"""
    assert deleteDuplicates([1, 2, 3, 2, 1, 5, 6, 5]) == [1, 2, 3, 5, 6]

def test_delete_duplicates_empty_list():
    """Test behavior with an empty list"""
    assert deleteDuplicates([]) == []

def test_delete_duplicates_all_same():
    """Test list with all identical elements"""
    assert deleteDuplicates([1, 1, 1, 1]) == [1]

def test_delete_duplicates_no_duplicates():
    """Test list with no duplicates"""
    assert deleteDuplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_delete_duplicates_order_preservation():
    """Test that the first occurrence of each element maintains its original position"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = [3, 1, 4, 5, 9, 2, 6]
    assert deleteDuplicates(input_list) == expected

def test_delete_duplicates_type_error():
    """Test that the function handles non-list inputs"""
    with pytest.raises(TypeError):
        deleteDuplicates("not a list")
    with pytest.raises(TypeError):
        deleteDuplicates(None)