import os
import pytest
import tempfile
import shutil

from src.file_merger import merge_files

def test_merge_files_basic():
    """Test basic merging of multiple files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create input files
        file1_path = os.path.join(tmpdir, 'file1.txt')
        file2_path = os.path.join(tmpdir, 'file2.txt')
        output_path = os.path.join(tmpdir, 'merged.txt')
        
        with open(file1_path, 'w') as f1:
            f1.write("Hello")
        
        with open(file2_path, 'w') as f2:
            f2.write("World")
        
        # Merge files
        merge_files([file1_path, file2_path], output_path)
        
        # Check merged content
        with open(output_path, 'r') as merged:
            assert merged.read() == "Hello\n\nWorld"

def test_merge_files_custom_separator():
    """Test merging with a custom separator."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create input files
        file1_path = os.path.join(tmpdir, 'file1.txt')
        file2_path = os.path.join(tmpdir, 'file2.txt')
        output_path = os.path.join(tmpdir, 'merged.txt')
        
        with open(file1_path, 'w') as f1:
            f1.write("Hello")
        
        with open(file2_path, 'w') as f2:
            f2.write("World")
        
        # Merge files with custom separator
        merge_files([file1_path, file2_path], output_path, separator=' /// ')
        
        # Check merged content
        with open(output_path, 'r') as merged:
            assert merged.read() == "Hello /// World"

def test_merge_files_single_file():
    """Test merging a single file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create input file
        file_path = os.path.join(tmpdir, 'file.txt')
        output_path = os.path.join(tmpdir, 'merged.txt')
        
        with open(file_path, 'w') as f:
            f.write("Single file content")
        
        # Merge single file
        merge_files([file_path], output_path)
        
        # Check content
        with open(output_path, 'r') as merged:
            assert merged.read() == "Single file content"

def test_merge_files_error_cases():
    """Test various error cases."""
    with tempfile.TemporaryDirectory() as tmpdir:
        output_path = os.path.join(tmpdir, 'merged.txt')
        
        # Empty input list
        with pytest.raises(ValueError, match="input_files list cannot be empty"):
            merge_files([], output_path)
        
        # Non-existent file
        with pytest.raises(FileNotFoundError):
            merge_files([os.path.join(tmpdir, 'nonexistent.txt')], output_path)
        
        # Invalid input types
        with pytest.raises(TypeError, match="input_files must be a list of file paths"):
            merge_files("not a list", output_path)
        
        with pytest.raises(TypeError, match="output_file must be a string"):
            merge_files([os.path.join(tmpdir, 'file.txt')], 123)
        
        with pytest.raises(TypeError, match="separator must be a string"):
            merge_files([os.path.join(tmpdir, 'file.txt')], output_path, separator=123)

def test_merge_files_empty_files():
    """Test merging files with empty content."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create empty input files
        file1_path = os.path.join(tmpdir, 'file1.txt')
        file2_path = os.path.join(tmpdir, 'file2.txt')
        output_path = os.path.join(tmpdir, 'merged.txt')
        
        open(file1_path, 'w').close()  # Create empty file
        open(file2_path, 'w').close()  # Create another empty file
        
        # Merge empty files
        merge_files([file1_path, file2_path], output_path)
        
        # Check merged content
        with open(output_path, 'r') as merged:
            assert merged.read() == "\n\n"