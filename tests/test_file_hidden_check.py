import os
import pytest
import tempfile
import shutil

from src.file_hidden_check import is_file_hidden

def test_hidden_files_unix_style():
    """Test hidden files with dot prefix"""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a hidden file
        hidden_file = os.path.join(tmpdir, '.hidden_file.txt')
        with open(hidden_file, 'w') as f:
            f.write('test')
        
        assert is_file_hidden(hidden_file) == True

def test_non_hidden_files():
    """Test non-hidden files"""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a non-hidden file
        visible_file = os.path.join(tmpdir, 'visible_file.txt')
        with open(visible_file, 'w') as f:
            f.write('test')
        
        assert is_file_hidden(visible_file) == False

def test_file_not_found():
    """Test handling of non-existent files"""
    with tempfile.TemporaryDirectory() as tmpdir:
        non_existent_file = os.path.join(tmpdir, 'non_existent_file.txt')
        
        with pytest.raises(FileNotFoundError):
            is_file_hidden(non_existent_file)

def test_invalid_input():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        is_file_hidden(123)
    
    with pytest.raises(TypeError):
        is_file_hidden(None)