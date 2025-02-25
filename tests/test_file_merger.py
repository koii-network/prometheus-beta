import os
import pytest
import tempfile
from src.file_merger import merge_files

def test_merge_files_basic():
    """Test basic file merging functionality."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create input files
        input_files = [
            os.path.join(tmpdir, 'file1.txt'),
            os.path.join(tmpdir, 'file2.txt')
        ]
        
        with open(input_files[0], 'w') as f1:
            f1.write("Hello")
        
        with open(input_files[1], 'w') as f2:
            f2.write("World")
        
        output_file = os.path.join(tmpdir, 'merged.txt')
        
        # Merge files
        merge_files(input_files, output_file)
        
        # Verify merged content
        with open(output_file, 'r') as f:
            content = f.read()
            assert content == "Hello\n\nWorld"

def test_merge_files_custom_separator():
    """Test merging files with custom separator."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create input files
        input_files = [
            os.path.join(tmpdir, 'file1.txt'),
            os.path.join(tmpdir, 'file2.txt')
        ]
        
        with open(input_files[0], 'w') as f1:
            f1.write("Hello")
        
        with open(input_files[1], 'w') as f2:
            f2.write("World")
        
        output_file = os.path.join(tmpdir, 'merged.txt')
        
        # Merge files with custom separator
        merge_files(input_files, output_file, separator=' --- ')
        
        # Verify merged content
        with open(output_file, 'r') as f:
            content = f.read()
            assert content == "Hello --- World"

def test_merge_files_empty_inputs():
    """Test merging with empty input list raises ValueError."""
    output_file = 'output.txt'
    
    with pytest.raises(ValueError, match="At least one input file must be provided."):
        merge_files([], output_file)

def test_merge_files_nonexistent_input():
    """Test merging with nonexistent input file raises FileNotFoundError."""
    with tempfile.TemporaryDirectory() as tmpdir:
        output_file = os.path.join(tmpdir, 'merged.txt')
        
        with pytest.raises(FileNotFoundError):
            merge_files(['nonexistent_file.txt'], output_file)

def test_merge_files_multiple_inputs():
    """Test merging multiple input files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create input files
        input_files = [
            os.path.join(tmpdir, 'file1.txt'),
            os.path.join(tmpdir, 'file2.txt'),
            os.path.join(tmpdir, 'file3.txt')
        ]
        
        with open(input_files[0], 'w') as f1:
            f1.write("First")
        
        with open(input_files[1], 'w') as f2:
            f2.write("Second")
        
        with open(input_files[2], 'w') as f3:
            f3.write("Third")
        
        output_file = os.path.join(tmpdir, 'merged.txt')
        
        # Merge files
        merge_files(input_files, output_file)
        
        # Verify merged content
        with open(output_file, 'r') as f:
            content = f.read()
            assert content == "First\n\nSecond\n\nThird"