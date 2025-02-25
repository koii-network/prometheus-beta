import pytest
from src.progress_logger import log_progress

def test_log_progress_basic_list():
    """Test basic functionality with a list of items."""
    items = list(range(10))
    progress_items = list(log_progress(items, desc="Test"))
    assert progress_items == items

def test_log_progress_with_total():
    """Test progress bar with explicitly provided total."""
    items = list(range(5))
    progress_items = list(log_progress(items, total=5, desc="Total Test"))
    assert progress_items == items

def test_log_progress_invalid_iterable():
    """Test that non-iterable inputs raise TypeError."""
    with pytest.raises(TypeError, match="Input must be an iterable"):
        list(log_progress(42))

def test_log_progress_invalid_total():
    """Test that invalid total values raise ValueError."""
    with pytest.raises(ValueError, match="Total must be a positive integer"):
        items = list(range(5))
        list(log_progress(items, total=-1))
    
    with pytest.raises(ValueError, match="Total must be a positive integer"):
        items = list(range(5))
        list(log_progress(items, total=0))
    
    with pytest.raises(ValueError, match="Total must be a positive integer"):
        items = list(range(5))
        list(log_progress(items, total="not a number"))

def test_log_progress_generator():
    """Test that the function works with a generator."""
    def sample_generator():
        for i in range(3):
            yield i

    progress_items = list(log_progress(sample_generator(), desc="Generator Test"))
    assert progress_items == [0, 1, 2]

def test_log_progress_empty_iterable():
    """Test progress bar with an empty iterable."""
    items = []
    progress_items = list(log_progress(items, desc="Empty Test"))
    assert progress_items == []