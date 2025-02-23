import pytest
from src.mountain_range import create_mountain_range, Peak, MountainRange

def test_create_mountain_range_default():
    """Test creating a mountain range with default parameters"""
    mountain_range = create_mountain_range(num_peaks=3)
    
    assert isinstance(mountain_range, MountainRange)
    assert len(mountain_range.peaks) == 3
    assert mountain_range.name is not None
    
    # Check peak attributes
    for peak in mountain_range.peaks:
        assert isinstance(peak, Peak)
        assert isinstance(peak.name, str)
        assert 1000.0 <= peak.height <= 8848.0

def test_create_mountain_range_custom_name():
    """Test creating a mountain range with a custom name"""
    range_name = "Himalayan Peaks"
    mountain_range = create_mountain_range(num_peaks=2, range_name=range_name)
    
    assert mountain_range.name == range_name
    assert len(mountain_range.peaks) == 2

def test_create_mountain_range_custom_height_range():
    """Test creating a mountain range with custom height range"""
    min_height = 2000.0
    max_height = 5000.0
    mountain_range = create_mountain_range(num_peaks=4, min_height=min_height, max_height=max_height)
    
    for peak in mountain_range.peaks:
        assert min_height <= peak.height <= max_height

def test_create_mountain_range_invalid_num_peaks():
    """Test raising error for invalid number of peaks"""
    with pytest.raises(ValueError, match="Number of peaks must be at least 1"):
        create_mountain_range(num_peaks=0)

def test_create_mountain_range_invalid_height_range():
    """Test raising error for invalid height range"""
    with pytest.raises(ValueError, match="Minimum height must be less than maximum height"):
        create_mountain_range(num_peaks=3, min_height=5000.0, max_height=3000.0)

def test_create_mountain_range_unique_peaks():
    """Test that generated peaks have unique names"""
    mountain_range = create_mountain_range(num_peaks=5)
    peak_names = [peak.name for peak in mountain_range.peaks]
    
    assert len(peak_names) == len(set(peak_names)), "Peak names must be unique"