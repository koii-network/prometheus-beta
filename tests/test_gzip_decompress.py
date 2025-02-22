import os
import gzip
import pytest
from src.gzip_decompress import decompress_gzip_file

@pytest.fixture
def sample_gzip_file(tmp_path):
    # Create a sample gzip file for testing
    input_file = tmp_path / "sample.txt.gz"
    with gzip.open(input_file, 'wb') as f:
        f.write(b"Hello, this is a test file for gzip decompression!")
    return input_file

def test_decompress_gzip_file(sample_gzip_file, tmp_path):
    # Test basic decompression
    output_file = decompress_gzip_file(str(sample_gzip_file), str(tmp_path / "sample.txt"))
    
    # Verify file was created
    assert os.path.exists(output_file)
    
    # Verify content
    with open(output_file, 'rb') as f:
        content = f.read()
        assert content == b"Hello, this is a test file for gzip decompression!"

def test_decompress_default_output(sample_gzip_file):
    # Test decompression with default output path
    output_file = decompress_gzip_file(str(sample_gzip_file))
    
    # Verify file was created
    assert os.path.exists(output_file)
    assert output_file.endswith('sample.txt')

def test_file_not_found():
    # Test non-existent input file
    with pytest.raises(FileNotFoundError):
        decompress_gzip_file("/path/to/nonexistent/file.gz")

def test_invalid_gzip_file(tmp_path):
    # Create an invalid gzip file
    invalid_file = tmp_path / "invalid.gz"
    with open(invalid_file, 'wb') as f:
        f.write(b"This is not a valid gzip file")
    
    # Test decompression of invalid file
    with pytest.raises(IOError):
        decompress_gzip_file(str(invalid_file))