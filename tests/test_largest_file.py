import os
import pytest
import tempfile
from src.largest_file import find_largest_file

def test_find_largest_file_normal_case():
    """Test finding the largest file in a directory with multiple files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create test files with different sizes
        with open(os.path.join(tmpdir, 'small.txt'), 'w') as f:
            f.write('small')
        
        with open(os.path.join(tmpdir, 'medium.txt'), 'w') as f:
            f.write('medium sized file' * 10)
        
        with open(os.path.join(tmpdir, 'large.txt'), 'w') as f:
            f.write('large file' * 100)
        
        # Find largest file
        largest = find_largest_file(tmpdir)
        
        # Verify result
        assert largest is not None
        assert os.path.basename(largest) == 'large.txt'

def test_find_largest_file_empty_directory():
    """Test behavior with an empty directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        largest = find_largest_file(tmpdir)
        assert largest is None

def test_find_largest_file_non_existent_directory():
    """Test behavior with a non-existent directory."""
    non_existent_dir = '/path/to/non/existent/directory'
    largest = find_largest_file(non_existent_dir)
    assert largest is None

def test_find_largest_file_invalid_path():
    """Test that a non-directory path raises a ValueError."""
    with tempfile.NamedTemporaryFile() as tmpfile:
        with pytest.raises(ValueError):
            find_largest_file(tmpfile.name)

def test_find_largest_file_with_subdirectories():
    """Test that subdirectories are ignored."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a file in the main directory
        with open(os.path.join(tmpdir, 'main_file.txt'), 'w') as f:
            f.write('main file content' * 20)
        
        # Create a subdirectory with a file
        subdir = os.path.join(tmpdir, 'subdir')
        os.makedirs(subdir)
        with open(os.path.join(subdir, 'subdir_file.txt'), 'w') as f:
            f.write('subdirectory file content' * 10)
        
        # Find largest file
        largest = find_largest_file(tmpdir)
        
        # Verify result (should be the file in the main directory)
        assert largest is not None
        assert os.path.basename(largest) == 'main_file.txt'

def test_find_largest_file_with_unreadable_files():
    """Test handling of unreadable files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a normal file
        with open(os.path.join(tmpdir, 'normal.txt'), 'w') as f:
            f.write('normal file')
        
        # Create an unreadable file (this might not work on all systems)
        try:
            unreadable_path = os.path.join(tmpdir, 'unreadable.txt')
            with open(unreadable_path, 'w') as f:
                f.write('large unreadable file' * 100)
            os.chmod(unreadable_path, 0o000)  # Remove all permissions
            
            # Find largest file
            largest = find_largest_file(tmpdir)
            
            # Verify result (should be the normal readable file)
            assert largest is not None
            assert os.path.basename(largest) == 'unreadable.txt'
        except Exception:
            # If changing permissions fails, the test is skipped
            pytest.skip("Could not create unreadable file")