import os
import bz2
import pytest
from src.bzip2_compressor import compress_file

def test_compress_file(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("This is a test file for bzip2 compression.")
    
    # Compress the file
    compressed_path = compress_file(str(test_file))
    
    # Check compressed file exists
    assert os.path.exists(compressed_path)
    assert compressed_path.endswith('.bz2')
    
    # Check file can be decompressed correctly
    with bz2.open(compressed_path, 'rt') as f:
        decompressed_content = f.read()
    
    assert decompressed_content == "This is a test file for bzip2 compression."

def test_compress_file_with_custom_output(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Custom output test")
    
    # Compress to a specific output path
    custom_output = tmp_path / "custom_compressed.bz2"
    compressed_path = compress_file(str(test_file), str(custom_output))
    
    assert compressed_path == str(custom_output)
    
    # Check file can be decompressed
    with bz2.open(compressed_path, 'rt') as f:
        decompressed_content = f.read()
    
    assert decompressed_content == "Custom output test"

def test_compress_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        compress_file("/path/to/nonexistent/file.txt")

def test_compress_directory(tmp_path):
    with pytest.raises(IsADirectoryError):
        compress_file(str(tmp_path))