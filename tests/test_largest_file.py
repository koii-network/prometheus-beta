import os
import pytest
import tempfile
from src.largest_file import find_largest_file

def test_find_largest_file():
    # Create a temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create sample files with different sizes
        files = [
            ('small.txt', b'small'),           # 5 bytes
            ('medium.txt', b'medium file'),    # 11 bytes
            ('large.txt', b'large file content')  # 21 bytes
        ]
        
        for filename, content in files:
            with open(os.path.join(temp_dir, filename), 'wb') as f:
                f.write(content)
        
        # Find the largest file
        largest_path, largest_size = find_largest_file(temp_dir)
        
        # Assert the correct file is found
        assert os.path.basename(largest_path) == 'large.txt'
        assert largest_size == 21

def test_empty_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Empty directory should return None, 0
        result_path, result_size = find_largest_file(temp_dir)
        assert result_path is None
        assert result_size == 0

def test_nonexistent_directory():
    # Nonexistent directory should return None, 0
    result_path, result_size = find_largest_file('/path/to/nonexistent/directory')
    assert result_path is None
    assert result_size == 0

def test_invalid_input_types():
    # Test invalid input types
    with pytest.raises(TypeError):
        find_largest_file(123)
    
    with pytest.raises(ValueError):
        find_largest_file('')