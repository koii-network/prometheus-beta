import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from mountain_range import create_mountain_range, Mountain

def test_create_mountain_range_basic():
    """Test creating a mountain range with a specific number of peaks"""
    num_peaks = 5
    mountain_range = create_mountain_range(num_peaks)
    
    assert len(mountain_range) == num_peaks
    assert all(isinstance(mountain, Mountain) for mountain in mountain_range)

def test_create_mountain_range_unique_names():
    """Ensure each mountain in the range has a unique name"""
    num_peaks = 5
    mountain_range = create_mountain_range(num_peaks)
    
    mountain_names = [mountain.name for mountain in mountain_range]
    assert len(mountain_names) == len(set(mountain_names))

def test_create_mountain_range_height_bounds():
    """Verify that mountain heights are within expected bounds"""
    num_peaks = 10
    mountain_range = create_mountain_range(num_peaks)
    
    for mountain in mountain_range:
        assert 6000 <= mountain.height <= 8848

def test_create_mountain_range_location_bounds():
    """Check that mountain locations are within the Himalayan region"""
    num_peaks = 10
    mountain_range = create_mountain_range(num_peaks)
    
    for mountain in mountain_range:
        assert 26.0 <= mountain.latitude <= 30.0
        assert 86.0 <= mountain.longitude <= 88.0

def test_create_mountain_range_invalid_input():
    """Test handling of invalid input (zero or negative peaks)"""
    with pytest.raises(ValueError, match="Number of peaks must be at least 1"):
        create_mountain_range(0)
    
    with pytest.raises(ValueError, match="Number of peaks must be at least 1"):
        create_mountain_range(-5)