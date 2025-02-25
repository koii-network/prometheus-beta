import os
import pytest
import tempfile
import shutil

from src.directory_size import calculate_directory_total_size


def test_calculate_directory_total_size_empty_directory():
    """Test total size of an empty directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        assert calculate_directory_total_size(temp_dir) == 0


def test_calculate_directory_total_size_single_file():
    """Test total size with a single file."""
    with tempfile.TemporaryDirectory() as temp_dir:
        test_file_path = os.path.join(temp_dir, 'test.txt')
        with open(test_file_path, 'w') as f:
            f.write('Hello, World!')
        
        assert calculate_directory_total_size(temp_dir) == len('Hello, World!')


def test_calculate_directory_total_size_multiple_files():
    """Test total size with multiple files."""
    with tempfile.TemporaryDirectory() as temp_dir:
        files_content = ['file1', 'file2', 'file3']
        total_size = 0
        
        for i, content in enumerate(files_content):
            file_path = os.path.join(temp_dir, f'test{i}.txt')
            with open(file_path, 'w') as f:
                f.write(content)
            total_size += len(content)
        
        assert calculate_directory_total_size(temp_dir) == total_size


def test_calculate_directory_total_size_nested_directory():
    """Test total size including nested directories."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create nested directory structure
        nested_dir = os.path.join(temp_dir, 'nested')
        os.makedirs(nested_dir)
        
        files_content = {
            os.path.join(temp_dir, 'top_level.txt'): 'top level',
            os.path.join(nested_dir, 'nested_file.txt'): 'nested file'
        }
        
        total_size = 0
        for path, content in files_content.items():
            with open(path, 'w') as f:
                f.write(content)
            total_size += len(content)
        
        assert calculate_directory_total_size(temp_dir) == total_size


def test_calculate_directory_total_size_nonexistent_directory():
    """Test error handling for nonexistent directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        nonexistent_dir = os.path.join(temp_dir, 'nonexistent')
        
        with pytest.raises(FileNotFoundError):
            calculate_directory_total_size(nonexistent_dir)


def test_calculate_directory_total_size_not_a_directory():
    """Test error handling when path is not a directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        test_file = os.path.join(temp_dir, 'test.txt')
        with open(test_file, 'w') as f:
            f.write('test')
        
        with pytest.raises(NotADirectoryError):
            calculate_directory_total_size(test_file)