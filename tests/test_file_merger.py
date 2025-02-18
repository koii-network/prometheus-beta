import os
import pytest
from src.file_merger import merge_files

@pytest.fixture
def sample_files(tmp_path):
    """Create sample files for testing"""
    file1 = tmp_path / "file1.txt"
    file1.write_text("Hello from file 1")
    
    file2 = tmp_path / "file2.txt"
    file2.write_text("Greetings from file 2")
    
    file3 = tmp_path / "file3.txt"
    file3.write_text("Salutations from file 3")
    
    return [str(file1), str(file2), str(file3)]

def test_merge_files_basic(sample_files, tmp_path):
    """Test basic merging of files"""
    output_file = str(tmp_path / "merged.txt")
    result = merge_files(sample_files, output_file)
    
    assert result == output_file
    with open(output_file, 'r') as f:
        content = f.read()
    
    assert "Hello from file 1" in content
    assert "Greetings from file 2" in content
    assert "Salutations from file 3" in content

def test_merge_files_custom_separator(sample_files, tmp_path):
    """Test merging with custom separator"""
    output_file = str(tmp_path / "merged_custom.txt")
    result = merge_files(sample_files, output_file, separator=" || ")
    
    with open(output_file, 'r') as f:
        content = f.read()
    
    assert " || " in content

def test_merge_files_empty_input():
    """Test that an empty input list raises ValueError"""
    with pytest.raises(ValueError, match="No input files provided"):
        merge_files([], "output.txt")

def test_merge_files_nonexistent_input(tmp_path):
    """Test that nonexistent files raise FileNotFoundError"""
    with pytest.raises(FileNotFoundError, match="Input file not found"):
        merge_files(["/path/to/nonexistent/file.txt"], str(tmp_path / "output.txt"))

def test_merge_files_single_file(sample_files, tmp_path):
    """Test merging a single file"""
    output_file = str(tmp_path / "single_merged.txt")
    result = merge_files([sample_files[0]], output_file)
    
    with open(output_file, 'r') as f:
        content = f.read()
    
    assert content.strip() == "Hello from file 1"