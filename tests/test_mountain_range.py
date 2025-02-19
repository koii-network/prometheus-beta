import pytest
from src.mountain_range import create_mountain_range, Mountain

def test_create_mountain_range_basic():
    """Test creating a mountain range with a standard number of peaks"""
    num_peaks = 5
    mountain_range = create_mountain_range(num_peaks)
    
    # Check the number of peaks
    assert len(mountain_range) == num_peaks
    
    # Check that each item is a Mountain object
    assert all(isinstance(mountain, Mountain) for mountain in mountain_range)

def test_create_mountain_range_single_peak():
    """Test creating a mountain range with a single peak"""
    num_peaks = 1
    mountain_range = create_mountain_range(num_peaks)
    
    assert len(mountain_range) == 1
    assert isinstance(mountain_range[0], Mountain)

def test_create_mountain_range_unique_names():
    """Test that mountain names are unique in the range"""
    num_peaks = 10
    mountain_range = create_mountain_range(num_peaks)
    
    names = [mountain.name for mountain in mountain_range]
    assert len(names) == len(set(names))

def test_mountain_object_attributes():
    """Test that Mountain objects have the correct attributes"""
    num_peaks = 3
    mountain_range = create_mountain_range(num_peaks)
    
    for mountain in mountain_range:
        assert hasattr(mountain, 'name')
        assert hasattr(mountain, 'height')
        assert hasattr(mountain, 'location')
        
        assert isinstance(mountain.name, str)
        assert isinstance(mountain.height, int)
        assert isinstance(mountain.location, str)
        
        # Check height constraints
        assert 4000 <= mountain.height <= 9000

def test_create_mountain_range_invalid_input():
    """Test that an error is raised for invalid number of peaks"""
    with pytest.raises(ValueError, match="Number of peaks must be at least 1"):
        create_mountain_range(0)
    
    with pytest.raises(ValueError, match="Number of peaks must be at least 1"):
        create_mountain_range(-1)