import os
import pytest
import tempfile
from src.zstandard_compression import compress_file, decompress_file

def create_test_file(content):
    """Helper function to create a temporary test file."""
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp_file:
        temp_file.write(content)
        return temp_file.name

def test_file_compression_and_decompression():
    # Create a test file with some content
    original_content = "This is a test file for Zstandard compression and decompression."
    original_file = create_test_file(original_content)
    
    try:
        # Compress the file
        compressed_file = compress_file(original_file)
        assert os.path.exists(compressed_file)
        assert compressed_file.endswith('.zst')
        
        # Decompress the file
        decompressed_file = decompress_file(compressed_file)
        assert os.path.exists(decompressed_file)
        
        # Verify content
        with open(decompressed_file, 'r') as f:
            decompressed_content = f.read()
        
        assert decompressed_content == original_content
    
    finally:
        # Clean up temporary files
        for file_path in [original_file, compressed_file, decompressed_file]:
            if os.path.exists(file_path):
                os.unlink(file_path)

def test_non_existent_file():
    with pytest.raises(FileNotFoundError):
        compress_file('/path/to/non/existent/file')

def test_compress_with_custom_output():
    # Create a test file with some content
    original_content = "Test file for custom output path"
    original_file = create_test_file(original_content)
    custom_output = original_file + '.custom.zst'
    
    try:
        # Compress with custom output path
        compressed_file = compress_file(original_file, custom_output)
        assert compressed_file == custom_output
        assert os.path.exists(compressed_file)
    
    finally:
        # Clean up temporary files
        for file_path in [original_file, custom_output]:
            if os.path.exists(file_path):
                os.unlink(file_path)

def test_decompress_with_custom_output():
    # Create a test file with some content
    original_content = "Test file for custom decompression output path"
    original_file = create_test_file(original_content)
    
    try:
        # Compress first
        compressed_file = compress_file(original_file)
        
        # Decompress with custom output path
        custom_output = '/tmp/decompressed_custom_file'
        decompressed_file = decompress_file(compressed_file, custom_output)
        
        assert decompressed_file == custom_output
        assert os.path.exists(decompressed_file)
        
        # Verify content
        with open(decompressed_file, 'r') as f:
            decompressed_content = f.read()
        
        assert decompressed_content == original_content
    
    finally:
        # Clean up temporary files
        for file_path in [original_file, compressed_file, custom_output]:
            if os.path.exists(file_path):
                os.unlink(file_path)