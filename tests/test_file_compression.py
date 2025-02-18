import os
import bz2
import pytest
from src.file_compression import compress_file_bzip2

def test_compress_file_bzip2_default_output(tmp_path):
    # Create a test file
    input_file = tmp_path / "test_input.txt"
    input_file.write_text("This is a test file for compression")
    
    # Compress the file
    compressed_file = compress_file_bzip2(str(input_file))
    
    # Check compressed file exists with .bz2 extension
    assert os.path.exists(compressed_file)
    assert compressed_file == str(input_file) + '.bz2'
    
    # Verify the file can be decompressed and content matches
    with bz2.open(compressed_file, 'rt') as f:
        content = f.read()
        assert content == "This is a test file for compression"

def test_compress_file_bzip2_custom_output(tmp_path):
    # Create a test file
    input_file = tmp_path / "test_input.txt"
    input_file.write_text("This is another test file")
    
    # Custom output path
    output_file = tmp_path / "custom_compressed.bz2"
    compressed_file = compress_file_bzip2(str(input_file), str(output_file))
    
    # Check compressed file exists at custom path
    assert os.path.exists(compressed_file)
    assert compressed_file == str(output_file)
    
    # Verify the file can be decompressed and content matches
    with bz2.open(compressed_file, 'rt') as f:
        content = f.read()
        assert content == "This is another test file"

def test_compress_nonexistent_file(tmp_path):
    # Try to compress a file that doesn't exist
    with pytest.raises(FileNotFoundError):
        compress_file_bzip2(str(tmp_path / "nonexistent.txt"))

def test_large_file(tmp_path):
    # Create a large file
    input_file = tmp_path / "large_file.txt"
    large_content = "x" * (1024 * 1024)  # 1MB of data
    input_file.write_text(large_content)
    
    # Compress the large file
    compressed_file = compress_file_bzip2(str(input_file))
    
    # Verify decompression
    with bz2.open(compressed_file, 'rt') as f:
        content = f.read()
        assert content == large_content