import os
import pytest
import tempfile
import shutil

from src.file_compression_ratio import calculate_compression_ratio

def create_test_files(original_content, compressed_content):
    """Helper function to create temporary test files."""
    # Create temporary directory
    temp_dir = tempfile.mkdtemp()
    
    # Create original file
    original_path = os.path.join(temp_dir, 'original.txt')
    with open(original_path, 'w') as f:
        f.write(original_content)
    
    # Create compressed file
    compressed_path = os.path.join(temp_dir, 'compressed.txt')
    with open(compressed_path, 'w') as f:
        f.write(compressed_content)
    
    return original_path, compressed_path, temp_dir

def test_compression_ratio_basic():
    """Test basic compression ratio calculation."""
    original_content = "Hello, world! " * 100
    compressed_content = "Hello, world! " * 50
    
    original_path, compressed_path, temp_dir = create_test_files(
        original_content, 
        compressed_content
    )
    
    try:
        ratio = calculate_compression_ratio(original_path, compressed_path)
        assert ratio == 2.0, f"Expected ratio 2.0, got {ratio}"
    finally:
        # Clean up temporary directory
        shutil.rmtree(temp_dir)

def test_compression_ratio_no_compression():
    """Test when compressed file is same size as original."""
    original_content = "No compression here"
    compressed_content = "No compression here"
    
    original_path, compressed_path, temp_dir = create_test_files(
        original_content, 
        compressed_content
    )
    
    try:
        ratio = calculate_compression_ratio(original_path, compressed_path)
        assert ratio == 1.0, f"Expected ratio 1.0, got {ratio}"
    finally:
        # Clean up temporary directory
        shutil.rmtree(temp_dir)

def test_file_not_found():
    """Test handling of non-existent files."""
    with pytest.raises(FileNotFoundError):
        calculate_compression_ratio('/path/to/nonexistent/original.txt', 
                                    '/path/to/nonexistent/compressed.txt')

def test_zero_size_files():
    """Test handling of zero-sized files."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create zero-sized files
        original_path = os.path.join(temp_dir, 'original.txt')
        compressed_path = os.path.join(temp_dir, 'compressed.txt')
        
        open(original_path, 'w').close()
        open(compressed_path, 'w').close()
        
        with pytest.raises(ValueError, match="file size must be greater than 0"):
            calculate_compression_ratio(original_path, compressed_path)

def test_compression_ratio_precision():
    """Test compression ratio with more complex scenario."""
    original_content = "A" * 1000
    compressed_content = "A" * 500
    
    original_path, compressed_path, temp_dir = create_test_files(
        original_content, 
        compressed_content
    )
    
    try:
        ratio = calculate_compression_ratio(original_path, compressed_path)
        assert abs(ratio - 2.0) < 1e-10, f"Expected ratio 2.0, got {ratio}"
    finally:
        # Clean up temporary directory
        shutil.rmtree(temp_dir)