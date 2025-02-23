import os
import pytest
import tempfile
from src.file_merger import merge_files

def test_merge_files_basic():
    """Test basic file merging functionality."""
    # Create temporary files
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create input files
        input1 = os.path.join(tmpdir, 'input1.txt')
        input2 = os.path.join(tmpdir, 'input2.txt')
        output = os.path.join(tmpdir, 'output.txt')
        
        with open(input1, 'w') as f1:
            f1.write("Hello")
        
        with open(input2, 'w') as f2:
            f2.write("World")
        
        # Merge files
        merge_files([input1, input2], output)
        
        # Verify output
        with open(output, 'r') as outfile:
            content = outfile.read()
            assert content == "Hello\nWorld"

def test_merge_files_custom_separator():
    """Test merging files with a custom separator."""
    with tempfile.TemporaryDirectory() as tmpdir:
        input1 = os.path.join(tmpdir, 'input1.txt')
        input2 = os.path.join(tmpdir, 'input2.txt')
        output = os.path.join(tmpdir, 'output.txt')
        
        with open(input1, 'w') as f1:
            f1.write("Hello")
        
        with open(input2, 'w') as f2:
            f2.write("World")
        
        # Merge files with custom separator
        merge_files([input1, input2], output, separator=' --- ')
        
        # Verify output
        with open(output, 'r') as outfile:
            content = outfile.read()
            assert content == "Hello --- World"

def test_merge_files_empty_list():
    """Test that an empty input list raises a ValueError."""
    with tempfile.TemporaryDirectory() as tmpdir:
        output = os.path.join(tmpdir, 'output.txt')
        
        with pytest.raises(ValueError, match="At least one input file must be provided"):
            merge_files([], output)

def test_merge_files_nonexistent_file():
    """Test that a nonexistent input file raises a FileNotFoundError."""
    with tempfile.TemporaryDirectory() as tmpdir:
        output = os.path.join(tmpdir, 'output.txt')
        nonexistent_file = os.path.join(tmpdir, 'nonexistent.txt')
        
        with pytest.raises(FileNotFoundError, match=f"Input file not found: {nonexistent_file}"):
            merge_files([nonexistent_file], output)

def test_merge_files_single_file():
    """Test merging a single file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        input_file = os.path.join(tmpdir, 'input.txt')
        output = os.path.join(tmpdir, 'output.txt')
        
        with open(input_file, 'w') as f:
            f.write("Single file content")
        
        # Merge single file
        merge_files([input_file], output)
        
        # Verify output
        with open(output, 'r') as outfile:
            content = outfile.read()
            assert content == "Single file content"