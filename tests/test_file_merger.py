import os
import pytest
from src.file_merger import merge_files

@pytest.fixture
def sample_files(tmp_path):
    """Create sample files for testing"""
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"
    
    file1.write_text("Hello from file 1\n")
    file2.write_text("Greetings from file 2\n")
    
    return [str(file1), str(file2)]

def test_merge_files_successful(sample_files, tmp_path):
    """Test successful file merging"""
    output_file = str(tmp_path / "merged.txt")
    result = merge_files(sample_files, output_file)
    
    assert result == output_file
    assert os.path.exists(output_file)
    
    with open(output_file, 'r') as f:
        content = f.read()
        assert "--- Contents of" in content
        assert "Hello from file 1" in content
        assert "Greetings from file 2" in content

def test_merge_files_empty_list():
    """Test merging with an empty input list"""
    with pytest.raises(ValueError, match="No input files provided"):
        merge_files([], "output.txt")

def test_merge_files_non_existent_file(tmp_path):
    """Test merging with non-existent files"""
    non_existent_file = str(tmp_path / "non_existent.txt")
    with pytest.raises(ValueError, match=f"The following files do not exist: ['{non_existent_file}']"):
        merge_files([non_existent_file], "output.txt")

def test_merge_files_no_permission(tmp_path):
    """Test handling of permission issues"""
    file1 = tmp_path / "file1.txt"
    file1.write_text("Test content")
    output_file = tmp_path / "output.txt"
    
    # Make output directory read-only to simulate permission issue
    output_file.parent.chmod(0o555)
    
    try:
        with pytest.raises(IOError):
            merge_files([str(file1)], str(output_file))
    finally:
        # Restore permissions
        output_file.parent.chmod(0o755)