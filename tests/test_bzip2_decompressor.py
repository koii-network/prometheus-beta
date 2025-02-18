import os
import bz2
import pytest
from src.bzip2_decompressor import decompress_bzip2_file

@pytest.fixture
def sample_bzip2_file(tmp_path):
    """Create a sample bzip2 compressed file for testing."""
    content = b"This is a test file for bzip2 decompression."
    compressed_file_path = tmp_path / "sample.txt.bz2"
    
    with bz2.open(compressed_file_path, 'wb') as f:
        f.write(content)
    
    return compressed_file_path

def test_decompress_bzip2_file_default_output(sample_bzip2_file, tmp_path):
    """Test decompression with default output filename."""
    output_path = decompress_bzip2_file(str(sample_bzip2_file))
    
    assert os.path.exists(output_path)
    with open(output_path, 'rb') as f:
        content = f.read()
    
    assert content == b"This is a test file for bzip2 decompression."

def test_decompress_bzip2_file_custom_output(sample_bzip2_file, tmp_path):
    """Test decompression with custom output filename."""
    custom_output = tmp_path / "custom_output.txt"
    output_path = decompress_bzip2_file(str(sample_bzip2_file), str(custom_output))
    
    assert output_path == str(custom_output)
    assert os.path.exists(output_path)
    with open(output_path, 'rb') as f:
        content = f.read()
    
    assert content == b"This is a test file for bzip2 decompression."

def test_decompress_bzip2_file_nonexistent_input(tmp_path):
    """Test handling of non-existent input file."""
    non_existent_file = tmp_path / "non_existent.txt.bz2"
    
    with pytest.raises(FileNotFoundError):
        decompress_bzip2_file(str(non_existent_file))