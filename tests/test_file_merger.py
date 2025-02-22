import os
import pytest
from src.file_merger import merge_files

def test_merge_files(tmpdir):
    # Create temporary input files
    p1 = tmpdir.join("file1.txt")
    p2 = tmpdir.join("file2.txt")
    p3 = tmpdir.join("file3.txt")
    output = tmpdir.join("merged.txt")
    
    p1.write("Hello\n")
    p2.write("World\n")
    p3.write("Python\n")
    
    # Merge files
    result = merge_files([str(p1), str(p2), str(p3)], str(output))
    
    # Check merge result
    assert result == str(output)
    assert os.path.exists(str(output))
    
    # Read merged file contents
    with open(str(output), 'r') as f:
        content = f.read()
    
    # Verify content
    assert content.strip() == "Hello\nWorld\nPython"

def test_merge_empty_list():
    # Test merging with empty input list
    with pytest.raises(ValueError, match="No input files provided"):
        merge_files([], "output.txt")

def test_merge_nonexistent_file(tmpdir):
    # Test merging with nonexistent file
    nonexistent_file = str(tmpdir.join("nonexistent.txt"))
    
    with pytest.raises(FileNotFoundError):
        merge_files([nonexistent_file], str(tmpdir.join("output.txt")))

def test_merge_single_file(tmpdir):
    # Test merging a single file
    input_file = tmpdir.join("input.txt")
    output_file = tmpdir.join("output.txt")
    
    input_file.write("Single file content")
    
    result = merge_files([str(input_file)], str(output_file))
    
    assert result == str(output_file)
    
    with open(str(output_file), 'r') as f:
        content = f.read()
    
    assert content.strip() == "Single file content"