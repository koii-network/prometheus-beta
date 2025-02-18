import os
import pytest
from src.file_merger import merge_files

def test_merge_files_basic(tmp_path):
    # Prepare test files
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"
    output_file = tmp_path / "merged.txt"
    
    file1.write_text("Hello")
    file2.write_text("World")
    
    # Merge files
    result = merge_files([str(file1), str(file2)], str(output_file))
    
    # Verify
    assert result == str(output_file)
    assert output_file.read_text() == "Hello\nWorld"

def test_merge_files_custom_separator(tmp_path):
    # Prepare test files
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"
    output_file = tmp_path / "merged.txt"
    
    file1.write_text("Hello")
    file2.write_text("World")
    
    # Merge files with custom separator
    result = merge_files([str(file1), str(file2)], str(output_file), separator=' | ')
    
    # Verify
    assert result == str(output_file)
    assert output_file.read_text() == "Hello | World"

def test_merge_files_empty_input():
    # Test empty input files list
    with pytest.raises(ValueError, match="No input files provided for merging"):
        merge_files([], "output.txt")

def test_merge_files_nonexistent_file(tmp_path):
    # Test with non-existent file
    output_file = tmp_path / "merged.txt"
    
    with pytest.raises(FileNotFoundError):
        merge_files(["/path/to/nonexistent/file.txt"], str(output_file))

def test_merge_multiple_files(tmp_path):
    # Prepare test files
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"
    file3 = tmp_path / "file3.txt"
    output_file = tmp_path / "merged.txt"
    
    file1.write_text("First")
    file2.write_text("Second")
    file3.write_text("Third")
    
    # Merge files
    result = merge_files([str(file1), str(file2), str(file3)], str(output_file))
    
    # Verify
    assert result == str(output_file)
    assert output_file.read_text() == "First\nSecond\nThird"