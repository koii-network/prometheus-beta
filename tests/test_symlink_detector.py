import os
import pytest
import tempfile
from src.symlink_detector import is_symbolic_link

def test_is_symbolic_link():
    # Test with a temporary directory and files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Regular file
        regular_file = os.path.join(temp_dir, 'regular_file.txt')
        with open(regular_file, 'w') as f:
            f.write('Test content')
        assert not is_symbolic_link(regular_file), "Regular file incorrectly identified as symlink"

        # Create a symbolic link
        symlink_path = os.path.join(temp_dir, 'my_symlink')
        target_file = os.path.join(temp_dir, 'target_file.txt')
        with open(target_file, 'w') as f:
            f.write('Target content')
        os.symlink(target_file, symlink_path)
        assert is_symbolic_link(symlink_path), "Symbolic link not detected"

def test_is_symbolic_link_error_handling():
    # Test invalid inputs
    with pytest.raises(ValueError, match="File path must be a non-empty string"):
        is_symbolic_link("")
    
    with pytest.raises(ValueError, match="File path must be a non-empty string"):
        is_symbolic_link(None)
    
    # Test non-existent path
    with pytest.raises(FileNotFoundError):
        is_symbolic_link("/path/to/non/existent/file")

def test_is_symbolic_link_expanded_path():
    # Test with user path expansion and absolute path resolution
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a symbolic link using a relative path
        os.chdir(temp_dir)
        target_file = 'target_file.txt'
        symlink_file = 'my_symlink'
        
        with open(target_file, 'w') as f:
            f.write('Test content')
        
        os.symlink(target_file, symlink_file)
        
        # Test both relative and absolute paths
        assert is_symbolic_link(symlink_file), "Relative symlink path not detected"
        assert is_symbolic_link(os.path.abspath(symlink_file)), "Absolute symlink path not detected"