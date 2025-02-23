import pytest
from src.find_single_non_duplicate import find_single_non_duplicate

def test_find_single_non_duplicate():
    # Test basic scenarios
    assert find_single_non_duplicate([1, 1, 2, 3, 3]) == 2
    assert find_single_non_duplicate([1, 1, 2, 2, 3, 4, 4]) == 3
    
    # Test single element array
    assert find_single_non_duplicate([5]) == 5
    
    # Test single non-duplicate at different positions
    assert find_single_non_duplicate([1, 1, 3, 4, 4, 5, 5]) == 3
    assert find_single_non_duplicate([1, 1, 2, 2, 3, 3, 4]) == 4
    
    # Edge cases
    with pytest.raises(TypeError):
        find_single_non_duplicate(None)
    
    with pytest.raises(TypeError):
        find_single_non_duplicate("not a list")
    
    with pytest.raises(ValueError):
        find_single_non_duplicate([])
    
    # Larger test case
    assert find_single_non_duplicate([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 7]) == 6