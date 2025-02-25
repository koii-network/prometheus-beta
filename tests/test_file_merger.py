import os
import pytest
import tempfile
import shutil

from src.file_merger import merge_files

def create_temp_file(content=''):
    """Helper function to create a temporary file with given content."""
    fd, path = tempfile.mkstemp(text=True)
    with open(path, 'w') as temp_file:
        temp_file.write(content)
    return path

def test_merge_files_basic():
    """Test basic file merging functionality."""
    # Create temporary files
    file1 = create_temp_file('Hello\n')
    file2 = create_temp_file('World\n')
    output = tempfile.mktemp()
    
    try:
        # Merge files
        merge_files([file1, file2], output)
        
        # Check output
        with open(output, 'r') as f:
            content = f.read()
        assert content == 'Hello\nWorld\n'
    finally:
        # Clean up temporary files
        os.unlink(file1)
        os.unlink(file2)
        if os.path.exists(output):
            os.unlink(output)

def test_merge_files_empty_list():
    """Test that merging an empty list of files raises an error."""
    output = tempfile.mktemp()
    
    with pytest.raises(ValueError, match="At least one input file must be provided."):
        merge_files([], output)

def test_merge_files_nonexistent_input():
    """Test that trying to merge a nonexistent file raises an error."""
    output = tempfile.mktemp()
    
    with pytest.raises(FileNotFoundError):
        merge_files(['/path/to/nonexistent/file.txt'], output)

def test_merge_files_overwrite():
    """Test overwrite functionality."""
    # Create temporary files
    file1 = create_temp_file('First content\n')
    file2 = create_temp_file('Second content\n')
    output = tempfile.mktemp()
    
    try:
        # First merge
        merge_files([file1], output)
        
        # Merge with overwrite
        merge_files([file2], output, overwrite=True)
        
        # Check output
        with open(output, 'r') as f:
            content = f.read()
        assert content == 'Second content\n'
    finally:
        # Clean up temporary files
        os.unlink(file1)
        os.unlink(file2)
        if os.path.exists(output):
            os.unlink(output)

def test_merge_files_existing_without_overwrite():
    """Test that merging to an existing file without overwrite raises an error."""
    # Create temporary files
    file1 = create_temp_file('Content\n')
    output = tempfile.mktemp()
    
    try:
        # First merge
        merge_files([file1], output)
        
        # Try to merge again without overwrite
        with pytest.raises(FileExistsError):
            merge_files([file1], output)
    finally:
        # Clean up temporary files
        os.unlink(file1)
        if os.path.exists(output):
            os.unlink(output)

def test_merge_files_no_trailing_newline():
    """Test merging files without trailing newlines."""
    # Create temporary files
    file1 = create_temp_file('First line')  # No newline
    file2 = create_temp_file('Second line')  # No newline
    output = tempfile.mktemp()
    
    try:
        # Merge files
        merge_files([file1, file2], output)
        
        # Check output
        with open(output, 'r') as f:
            content = f.read()
        assert content == 'First line\nSecond line\n'
    finally:
        # Clean up temporary files
        os.unlink(file1)
        os.unlink(file2)
        if os.path.exists(output):
            os.unlink(output)