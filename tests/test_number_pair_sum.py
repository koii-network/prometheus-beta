import pytest
import os
import tempfile

from src.number_pair_sum import sum_pairs_with_nine_diff

def test_basic_pair_sum():
    """Test basic scenario with pairs having 9 difference."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("10\n1\n19\n28\n37\n46\n")
        temp_file.close()
        
        try:
            result = sum_pairs_with_nine_diff(temp_file.name)
            assert result == 72  # (10+1) + (19+28)
        finally:
            os.unlink(temp_file.name)

def test_empty_file():
    """Test behavior with an empty file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.close()
        
        try:
            result = sum_pairs_with_nine_diff(temp_file.name)
            assert result == 0
        finally:
            os.unlink(temp_file.name)

def test_no_matching_pairs():
    """Test scenario with no pairs having 9 difference."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("1\n2\n3\n4\n5\n")
        temp_file.close()
        
        try:
            result = sum_pairs_with_nine_diff(temp_file.name)
            assert result == 0
        finally:
            os.unlink(temp_file.name)

def test_multiple_matching_pairs():
    """Test scenario with multiple matching pairs."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("1\n10\n19\n28\n37\n46\n55\n")
        temp_file.close()
        
        try:
            result = sum_pairs_with_nine_diff(temp_file.name)
            assert result == 144  # (1+10) + (19+28) + (37+46)
        finally:
            os.unlink(temp_file.name)

def test_file_not_found():
    """Test error handling for non-existent file."""
    with pytest.raises(FileNotFoundError):
        sum_pairs_with_nine_diff("non_existent_file.txt")

def test_invalid_file_contents():
    """Test error handling for non-numeric file contents."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("1\n2\n3\nabc\n4\n")
        temp_file.close()
        
        try:
            with pytest.raises(ValueError):
                sum_pairs_with_nine_diff(temp_file.name)
        finally:
            os.unlink(temp_file.name)