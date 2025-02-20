import os
import gzip
import pytest
from src.gzip_decompression import decompress_gzip_file

def test_decompress_basic(tmp_path):
    # Create a sample gzip file
    input_data = b"Hello, this is a test file for gzip decompression!"
    input_file = tmp_path / "test_input.txt.gz"
    with gzip.open(input_file, 'wb') as f:
        f.write(input_data)
    
    # Decompress the file
    output_file = decompress_gzip_file(str(input_file))
    
    # Verify contents
    with open(output_file, 'rb') as f:
        assert f.read() == input_data

def test_decompress_custom_output(tmp_path):
    # Create a sample gzip file
    input_data = b"Custom output test data"
    input_file = tmp_path / "test_custom.txt.gz"
    output_file = tmp_path / "custom_output.txt"
    
    with gzip.open(input_file, 'wb') as f:
        f.write(input_data)
    
    # Decompress to custom output
    result_file = decompress_gzip_file(str(input_file), str(output_file))
    
    # Verify contents and path
    assert result_file == str(output_file)
    with open(result_file, 'rb') as f:
        assert f.read() == input_data

def test_decompress_nonexistent_file():
    # Test file not found scenario
    with pytest.raises(FileNotFoundError):
        decompress_gzip_file("nonexistent_file.txt.gz")

def test_decompress_corrupted_file(tmp_path):
    # Create a corrupted gzip file
    input_file = tmp_path / "corrupted.txt.gz"
    with open(input_file, 'wb') as f:
        f.write(b"This is not a valid gzip file")
    
    # Attempt to decompress should raise an IOError
    with pytest.raises(IOError):
        decompress_gzip_file(str(input_file))