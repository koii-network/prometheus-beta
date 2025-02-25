import os
import pytest
import tempfile
import pathlib

from src.directory_size import get_total_directory_size

def test_empty_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        assert get_total_directory_size(temp_dir) == 0

def test_single_file_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a test file
        test_file_path = os.path.join(temp_dir, 'test.txt')
        with open(test_file_path, 'w') as f:
            f.write('Hello, World!')
        
        # Expected size is length of 'Hello, World!'
        assert get_total_directory_size(temp_dir) == len('Hello, World!')

def test_multiple_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create multiple files
        files_content = ['file1 content', 'file2 content longer', 'another file']
        for i, content in enumerate(files_content):
            with open(os.path.join(temp_dir, f'test{i}.txt'), 'w') as f:
                f.write(content)
        
        # Calculate expected total size
        expected_size = sum(len(content) for content in files_content)
        assert get_total_directory_size(temp_dir) == expected_size

def test_nested_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create nested directories with files
        nested_dir = os.path.join(temp_dir, 'nested')
        os.makedirs(nested_dir)
        
        files_content = ['nested file 1', 'nested file 2']
        for i, content in enumerate(files_content):
            with open(os.path.join(nested_dir, f'nested_test{i}.txt'), 'w') as f:
                f.write(content)
        
        # Calculate expected total size
        expected_size = sum(len(content) for content in files_content)
        assert get_total_directory_size(temp_dir) == expected_size

def test_invalid_input_types():
    with pytest.raises(TypeError):
        get_total_directory_size(123)
    
    with pytest.raises(TypeError):
        get_total_directory_size(None)

def test_nonexistent_directory():
    with pytest.raises(FileNotFoundError):
        get_total_directory_size('/path/to/nonexistent/directory')

def test_not_a_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a file
        test_file = os.path.join(temp_dir, 'test.txt')
        with open(test_file, 'w') as f:
            f.write('test')
        
        with pytest.raises(NotADirectoryError):
            get_total_directory_size(test_file)