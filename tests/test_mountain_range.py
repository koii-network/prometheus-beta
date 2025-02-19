import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from mountain_range import create_mountain_range, Mountain

def test_create_mountain_range_zero_peaks():
    """Test creating a mountain range with zero peaks"""
    mountain_range = create_mountain_range(0)
    assert len(mountain_range) == 0

def test_create_mountain_range_multiple_peaks():
    """Test creating a mountain range with multiple peaks"""
    num_peaks = 5
    mountain_range = create_mountain_range(num_peaks)
    
    assert len(mountain_range) == num_peaks
    
    for mountain in mountain_range:
        # Check that each mountain is an instance of Mountain class
        assert isinstance(mountain, Mountain)
        
        # Check name is not empty
        assert mountain.name is not None
        assert len(mountain.name) > 0
        
        # Check height is within specified range (using default parameters)
        assert 1000 <= mountain.height <= 8848
        
        # Check latitude is within valid range
        assert -90 <= mountain.latitude <= 90
        
        # Check longitude is within valid range
        assert -180 <= mountain.longitude <= 180

def test_create_mountain_range_invalid_peaks():
    """Test creating a mountain range with negative number of peaks"""
    with pytest.raises(ValueError, match="Number of peaks must be non-negative"):
        create_mountain_range(-1)

def test_create_mountain_range_custom_parameters():
    """Test creating a mountain range with custom parameters"""
    num_peaks = 3
    min_height = 2000
    max_height = 5000
    latitude_range = (20, 40)
    longitude_range = (-100, -80)
    
    mountain_range = create_mountain_range(
        num_peaks, 
        min_height=min_height, 
        max_height=max_height, 
        latitude_range=latitude_range, 
        longitude_range=longitude_range
    )
    
    assert len(mountain_range) == num_peaks
    
    for mountain in mountain_range:
        assert min_height <= mountain.height <= max_height
        assert latitude_range[0] <= mountain.latitude <= latitude_range[1]
        assert longitude_range[0] <= mountain.longitude <= longitude_range[1]

def test_mountain_object_creation():
    """Test Mountain object creation"""
    name = "Test Peak"
    height = 3000
    latitude = 45.5
    longitude = -120.3
    
    mountain = Mountain(name, height, latitude, longitude)
    
    assert mountain.name == name
    assert mountain.height == height
    assert mountain.latitude == latitude
    assert mountain.longitude == longitude