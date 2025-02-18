import os
import pytest
from src.file_merger import merge_files

def test_merge_files(tmp_path):
    # Create test input files
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"
    file3 = tmp_path / "file3.txt"
    output_file = tmp_path / "merged.txt"
    
    # Write content to test files
    file1.write_text("Hello\n")
    file2.write_text("World\n")
    file3.write_text("Merge Test")
    
    # Perform file merge
    result = merge_files([str(file1), str(file2), str(file3)], str(output_file))
    
    # Verify the result
    assert result == str(output_file)
    assert os.path.exists(output_file)
    
    # Check merged file contents
    with open(output_file, 'r') as f:
        content = f.read()
    
    assert content == "Hello\nWorld\nMerge Test"

def test_merge_files_empty_list():
    # Test that an empty list raises a ValueError
    with pytest.raises(ValueError):
        merge_files([], "output.txt")

def test_merge_files_nonexistent_input():
    # Test that a nonexistent input file raises FileNotFoundError
    with pytest.raises(FileNotFoundError):
        merge_files(["nonexistent_file.txt"], "output.txt")

def test_merge_single_file(tmp_path):
    # Test merging a single file
    input_file = tmp_path / "input.txt"
    output_file = tmp_path / "output.txt"
    
    input_file.write_text("Single File Test")
    
    result = merge_files([str(input_file)], str(output_file))
    
    with open(output_file, 'r') as f:
        content = f.read()
    
    assert content == "Single File Test"