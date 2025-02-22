import os
import bz2
import pytest
from src.bzip2_decompress import decompress_bzip2_file

@pytest.fixture
def sample_bz2_file(tmp_path):
    """Create a sample bzip2 compressed file for testing"""
    sample_content = b"This is a test file for bzip2 decompression."
    input_file = tmp_path / "sample.txt.bz2"
    
    with bz2.open(input_file, 'wb') as f:
        f.write(sample_content)
    
    return input_file

def test_decompress_bzip2_file_default_output(sample_bz2_file, tmp_path):
    """Test decompression with default output path"""
    output_path = decompress_bzip2_file(str(sample_bz2_file))
    
    assert os.path.exists(output_path)
    with open(output_path, 'rb') as f:
        content = f.read()
    
    assert content == b"This is a test file for bzip2 decompression."

def test_decompress_bzip2_file_custom_output(sample_bz2_file, tmp_path):
    """Test decompression with custom output path"""
    custom_output = str(tmp_path / "custom_output.txt")
    output_path = decompress_bzip2_file(str(sample_bz2_file), custom_output)
    
    assert output_path == custom_output
    assert os.path.exists(output_path)
    with open(output_path, 'rb') as f:
        content = f.read()
    
    assert content == b"This is a test file for bzip2 decompression."

def test_decompress_nonexistent_file():
    """Test handling of non-existent input file"""
    with pytest.raises(FileNotFoundError):
        decompress_bzip2_file("/path/to/nonexistent/file.bz2")

def test_decompress_directory():
    """Test handling of directory input"""
    with pytest.raises(IsADirectoryError):
        decompress_bzip2_file("/tmp")  # Assuming /tmp exists as a directory