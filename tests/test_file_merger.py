import os
import pytest
import sys
import tempfile

# Add the src directory to the Python path
sys.path.append(os.path.abspath('src'))

from file_merger import merge_files

def test_merge_files_basic():
    # Create temporary input and output files
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create input files
        input_file1 = os.path.join(tmpdir, 'file1.txt')
        input_file2 = os.path.join(tmpdir, 'file2.txt')
        output_file = os.path.join(tmpdir, 'merged.txt')
        
        with open(input_file1, 'w') as f1:
            f1.write("Hello from file 1")
        
        with open(input_file2, 'w') as f2:
            f2.write("Hello from file 2")
        
        # Merge files
        result = merge_files([input_file1, input_file2], output_file)
        
        # Check output
        assert result == output_file
        with open(output_file, 'r') as merged:
            content = merged.read()
            assert "Hello from file 1" in content
            assert "Hello from file 2" in content
            assert content.count("\n\n") == 1  # default separator

def test_merge_files_custom_separator():
    with tempfile.TemporaryDirectory() as tmpdir:
        input_file1 = os.path.join(tmpdir, 'file1.txt')
        input_file2 = os.path.join(tmpdir, 'file2.txt')
        output_file = os.path.join(tmpdir, 'merged.txt')
        
        with open(input_file1, 'w') as f1:
            f1.write("Hello from file 1")
        
        with open(input_file2, 'w') as f2:
            f2.write("Hello from file 2")
        
        # Merge files with custom separator
        result = merge_files([input_file1, input_file2], output_file, separator='---')
        
        with open(output_file, 'r') as merged:
            content = merged.read()
            assert "Hello from file 1" in content
            assert "Hello from file 2" in content
            assert "---" in content

def test_merge_files_empty_input():
    with tempfile.TemporaryDirectory() as tmpdir:
        output_file = os.path.join(tmpdir, 'merged.txt')
        
        # Should raise ValueError for empty input list
        with pytest.raises(ValueError, match="No input files provided"):
            merge_files([], output_file)

def test_merge_files_nonexistent_file():
    with tempfile.TemporaryDirectory() as tmpdir:
        output_file = os.path.join(tmpdir, 'merged.txt')
        
        # Should raise FileNotFoundError for non-existent input file
        with pytest.raises(FileNotFoundError, match="Input file not found"):
            merge_files(['/path/to/nonexistent/file.txt'], output_file)