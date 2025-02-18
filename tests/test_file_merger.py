import os
import pytest
from src.file_merger import merge_files

@pytest.fixture
def sample_files(tmp_path):
    # Create sample files for testing
    file1 = tmp_path / "file1.txt"
    file1.write_text("Hello\n")
    file2 = tmp_path / "file2.txt"
    file2.write_text("World\n")
    file3 = tmp_path / "file3.txt"
    file3.write_text("Merged\n")
    
    return [str(file1), str(file2), str(file3)]

def test_merge_files_success(sample_files, tmp_path):
    output_file = str(tmp_path / "merged.txt")
    
    # Merge files
    result = merge_files(sample_files, output_file)
    
    # Check the result
    assert result == output_file
    assert os.path.exists(output_file)
    
    # Check content of merged file
    with open(output_file, 'r') as f:
        content = f.read()
    
    expected_content = "Hello\nWorld\nMerged\n"
    assert content == expected_content

def test_merge_files_empty_list():
    with pytest.raises(ValueError, match="No input files provided"):
        merge_files([], "output.txt")

def test_merge_files_non_existent():
    with pytest.raises(ValueError, match="The following files do not exist"):
        merge_files(["/path/to/non/existent/file.txt"], "output.txt")

def test_merge_files_invalid_output_path(sample_files):
    with pytest.raises(IOError):
        merge_files(sample_files, "/invalid/path/output.txt")