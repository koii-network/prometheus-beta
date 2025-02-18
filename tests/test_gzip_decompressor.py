import os
import gzip
import pytest
from src.gzip_decompressor import decompress_gzip_file

@pytest.fixture
def sample_gzip_file(tmp_path):
    # Create a sample gzip file for testing
    test_content = b'This is a test file for gzip decompression.'
    gzip_path = tmp_path / 'test_file.txt.gz'
    
    with gzip.open(gzip_path, 'wb') as f:
        f.write(test_content)
    
    return gzip_path

def test_decompress_gzip_file_default_output(sample_gzip_file, tmp_path):
    # Test decompression with default output path
    decompressed_file = decompress_gzip_file(str(sample_gzip_file))
    
    assert os.path.exists(decompressed_file)
    assert decompressed_file.endswith('.txt')
    
    with open(decompressed_file, 'rb') as f:
        content = f.read()
        assert content == b'This is a test file for gzip decompression.'

def test_decompress_gzip_file_custom_output(sample_gzip_file, tmp_path):
    # Test decompression with custom output path
    output_path = tmp_path / 'custom_output.txt'
    decompressed_file = decompress_gzip_file(str(sample_gzip_file), str(output_path))
    
    assert os.path.exists(decompressed_file)
    assert decompressed_file == str(output_path)
    
    with open(decompressed_file, 'rb') as f:
        content = f.read()
        assert content == b'This is a test file for gzip decompression.'

def test_decompress_gzip_file_nonexistent_input():
    # Test handling of nonexistent input file
    with pytest.raises(FileNotFoundError):
        decompress_gzip_file('/path/to/nonexistent/file.gz')

def test_decompress_gzip_file_invalid_extension(tmp_path):
    # Test handling of non-gzip file
    invalid_file = tmp_path / 'test_file.txt'
    invalid_file.write_text('This is not a gzip file')
    
    with pytest.raises(ValueError):
        decompress_gzip_file(str(invalid_file))