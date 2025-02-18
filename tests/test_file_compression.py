import os
import bz2
import pytest
from src.file_compression import compress_file_bzip2

def test_compress_file_bzip2_default_output(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Hello, world!")
    
    # Compress the file
    compressed_path = compress_file_bzip2(str(test_file))
    
    # Check compressed file exists with .bz2 extension
    assert os.path.exists(compressed_path)
    assert compressed_path == str(test_file) + '.bz2'
    
    # Verify content can be decompressed correctly
    with bz2.open(compressed_path, 'rt') as f:
        assert f.read() == "Hello, world!"

def test_compress_file_bzip2_custom_output(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Custom output test")
    
    # Custom output path
    custom_output = tmp_path / "compressed_file.bz2"
    compressed_path = compress_file_bzip2(str(test_file), str(custom_output))
    
    # Check compressed file exists at custom path
    assert os.path.exists(compressed_path)
    assert compressed_path == str(custom_output)
    
    # Verify content can be decompressed correctly
    with bz2.open(compressed_path, 'rt') as f:
        assert f.read() == "Custom output test"

def test_compress_file_bzip2_nonexistent_file(tmp_path):
    # Test non-existent file raises FileNotFoundError
    with pytest.raises(FileNotFoundError):
        compress_file_bzip2(str(tmp_path / "nonexistent.txt"))

def test_compress_file_bzip2_directory(tmp_path):
    # Test attempting to compress a directory raises IsADirectoryError
    with pytest.raises(IsADirectoryError):
        compress_file_bzip2(str(tmp_path))