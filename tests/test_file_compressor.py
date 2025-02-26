import os
import bz2
import pytest
from src.file_compressor import compress_file_bzip2

def test_compress_file_bzip2_default_output(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_input.txt"
    test_file.write_text("This is a test file for compression")
    
    # Compress the file
    compressed_file = compress_file_bzip2(str(test_file))
    
    # Check compressed file exists with correct extension
    assert os.path.exists(compressed_file)
    assert compressed_file == str(test_file) + '.bz2'
    
    # Verify contents can be decompressed
    with bz2.open(compressed_file, 'rt') as f:
        assert f.read() == "This is a test file for compression"

def test_compress_file_bzip2_custom_output(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_input.txt"
    test_file.write_text("Custom output compression test")
    
    # Custom output file
    custom_output = tmp_path / "custom_compressed.bz2"
    
    # Compress the file
    compressed_file = compress_file_bzip2(str(test_file), str(custom_output))
    
    # Check compressed file exists at custom location
    assert os.path.exists(compressed_file)
    assert compressed_file == str(custom_output)
    
    # Verify contents can be decompressed
    with bz2.open(compressed_file, 'rt') as f:
        assert f.read() == "Custom output compression test"

def test_compress_file_bzip2_nonexistent_file(tmp_path):
    # Try to compress a file that doesn't exist
    with pytest.raises(FileNotFoundError):
        compress_file_bzip2(str(tmp_path / "nonexistent.txt"))

def test_compress_large_file(tmp_path):
    # Create a larger test file
    test_file = tmp_path / "large_test.txt"
    test_file.write_text("A" * (1024 * 1024))  # 1MB of data
    
    # Compress the file
    compressed_file = compress_file_bzip2(str(test_file))
    
    # Check compressed file exists
    assert os.path.exists(compressed_file)
    
    # Verify contents can be decompressed
    with bz2.open(compressed_file, 'rt') as f:
        assert f.read() == "A" * (1024 * 1024)