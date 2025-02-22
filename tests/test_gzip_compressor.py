import os
import gzip
import pytest
from src.gzip_compressor import compress_file

def test_compress_file(tmp_path):
    # Create a test file
    input_file = tmp_path / "test_file.txt"
    input_file.write_text("This is a test file for compression")
    input_file_path = str(input_file)
    
    # Test default compression (appending .gz)
    compressed_file_path = compress_file(input_file_path)
    
    # Verify compressed file was created
    assert os.path.exists(compressed_file_path)
    assert compressed_file_path.endswith('.gz')
    
    # Verify file can be decompressed
    with gzip.open(compressed_file_path, 'rt') as f:
        decompressed_content = f.read()
    
    assert decompressed_content == "This is a test file for compression"

def test_compress_file_with_custom_output(tmp_path):
    # Create a test file
    input_file = tmp_path / "test_file.txt"
    input_file.write_text("Custom output test")
    input_file_path = str(input_file)
    
    # Custom output path
    output_file = tmp_path / "custom_compressed.gz"
    output_file_path = str(output_file)
    
    # Compress with custom output
    compressed_file_path = compress_file(input_file_path, output_file_path)
    
    # Verify compressed file was created at specified location
    assert compressed_file_path == output_file_path
    assert os.path.exists(compressed_file_path)
    
    # Verify file can be decompressed
    with gzip.open(compressed_file_path, 'rt') as f:
        decompressed_content = f.read()
    
    assert decompressed_content == "Custom output test"

def test_compress_nonexistent_file(tmp_path):
    # Test file not found scenario
    with pytest.raises(FileNotFoundError):
        compress_file(str(tmp_path / "nonexistent_file.txt"))