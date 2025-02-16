import os
import pytest
import lzma
import tempfile
import shutil

from src.xz_compression import compress_to_xz

def test_compress_to_xz_simple_file():
    # Create a temporary file with known content
    with tempfile.NamedTemporaryFile(delete=False) as temp_input:
        test_content = b"Hello, XZ compression test!"
        temp_input.write(test_content)
        temp_input.close()
    
    try:
        # Compress the file
        compressed_path = compress_to_xz(temp_input.name)
        
        # Verify compression
        assert os.path.exists(compressed_path)
        assert compressed_path.endswith('.xz')
        
        # Verify decompression works
        with lzma.open(compressed_path, 'rb') as decomp_file:
            decompressed_content = decomp_file.read()
        
        assert decompressed_content == test_content
    finally:
        # Clean up files
        os.unlink(temp_input.name)
        if os.path.exists(compressed_path):
            os.unlink(compressed_path)

def test_compress_to_xz_custom_output():
    # Create a temporary file with known content
    with tempfile.NamedTemporaryFile(delete=False) as temp_input:
        test_content = b"Custom output path test"
        temp_input.write(test_content)
        temp_input.close()
    
    # Create a custom output path
    with tempfile.NamedTemporaryFile(delete=False) as temp_output:
        temp_output.close()
    
    try:
        # Compress the file with custom output path
        compressed_path = compress_to_xz(temp_input.name, temp_output.name)
        
        # Verify compression
        assert os.path.exists(compressed_path)
        assert compressed_path == temp_output.name
        
        # Verify decompression works
        with lzma.open(compressed_path, 'rb') as decomp_file:
            decompressed_content = decomp_file.read()
        
        assert decompressed_content == test_content
    finally:
        # Clean up files
        os.unlink(temp_input.name)
        if os.path.exists(compressed_path):
            os.unlink(compressed_path)

def test_compress_to_xz_nonexistent_file():
    # Test handling of non-existent file
    with pytest.raises(FileNotFoundError):
        compress_to_xz('/path/to/nonexistent/file.txt')

def test_compress_to_xz_directory():
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()
    
    try:
        # Test that directory compression raises an error
        with pytest.raises(IsADirectoryError):
            compress_to_xz(temp_dir)
    finally:
        # Clean up
        shutil.rmtree(temp_dir)