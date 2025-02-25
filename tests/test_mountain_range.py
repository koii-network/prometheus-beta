import pytest
import random
from src.mountain_range import create_mountain_range, Mountain

def test_create_mountain_range_basic():
    """Test creating a mountain range with default parameters."""
    num_peaks = 5
    mountain_range = create_mountain_range(num_peaks)
    
    # Check number of peaks
    assert len(mountain_range) == num_peaks
    
    # Check type of returned objects
    assert all(isinstance(mountain, Mountain) for mountain in mountain_range)

def test_create_mountain_range_with_region():
    """Test creating a mountain range with a specific region."""
    num_peaks = 3
    region = "Himalayas"
    mountain_range = create_mountain_range(num_peaks, region)
    
    # Check number of peaks
    assert len(mountain_range) == num_peaks
    
    # Check region in mountain names
    assert all(f"({region})" in mountain.name for mountain in mountain_range)
    assert all(mountain.location == region for mountain in mountain_range)

def test_create_mountain_range_zero_peaks():
    """Test creating a mountain range with zero peaks."""
    mountain_range = create_mountain_range(0)
    assert len(mountain_range) == 0

def test_create_mountain_range_invalid_inputs():
    """Test error handling for invalid inputs."""
    # Test negative number of peaks
    with pytest.raises(ValueError, match="Number of peaks cannot be negative"):
        create_mountain_range(-1)
    
    # Test non-integer input
    with pytest.raises(TypeError, match="Number of peaks must be an integer"):
        create_mountain_range(3.5)
    with pytest.raises(TypeError, match="Number of peaks must be an integer"):
        create_mountain_range("5")

def test_mountain_height_range():
    """Test that mountain heights are within expected range."""
    num_peaks = 10
    mountain_range = create_mountain_range(num_peaks)
    
    # Check height ranges
    for mountain in mountain_range:
        assert 1000 <= mountain.height <= 8000, f"Mountain height {mountain.height} out of range"

def test_mountain_name_uniqueness():
    """Test that mountain names are unique with region."""
    num_peaks = 11  # More than predefined names
    region = "Alps"
    mountain_range = create_mountain_range(num_peaks, region)
    
    # Ensure mountain names have appended index
    names = [mountain.name for mountain in mountain_range]
    assert len(set(names)) == len(names), "Mountain names are not unique"