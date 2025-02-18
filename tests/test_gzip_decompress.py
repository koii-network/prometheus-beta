import os
import gzip
import pytest
from src.gzip_decompress import decompress_gzip_file

@pytest.fixture
def sample_gzip_file(tmp_path):
    """Create a sample gzip file for testing"""
    input_content = b"This is a test file for gzip decompression."
    input_file = tmp_path / "test_file.txt.gz"
    
    with gzip.open(input_file, 'wb') as f:
        f.write(input_content)
    
    return input_file

def test_decompress_gzip_file_default_output(sample_gzip_file, tmp_path):
    """Test decompression with default output path"""
    output_path = decompress_gzip_file(str(sample_gzip_file))
    
    assert os.path.exists(output_path)
    assert output_path == str(sample_gzip_file)[:-3]
    
    with open(output_path, 'rb') as f:
        assert f.read() == b"This is a test file for gzip decompression."

def test_decompress_gzip_file_custom_output(sample_gzip_file, tmp_path):
    """Test decompression with custom output path"""
    custom_output = str(tmp_path / "custom_output.txt")
    output_path = decompress_gzip_file(str(sample_gzip_file), custom_output)
    
    assert os.path.exists(output_path)
    assert output_path == custom_output
    
    with open(output_path, 'rb') as f:
        assert f.read() == b"This is a test file for gzip decompression."

def test_decompress_nonexistent_file():
    """Test handling of non-existent input file"""
    with pytest.raises(FileNotFoundError):
        decompress_gzip_file("nonexistent_file.txt.gz")

def test_decompress_non_gzip_file(tmp_path):
    """Test handling of non-gzip input file"""
    non_gzip_file = tmp_path / "test_file.txt"
    non_gzip_file.write_text("This is not a gzip file")
    
    with pytest.raises(ValueError):
        decompress_gzip_file(str(non_gzip_file))