import os
import pytest
import tempfile
import random
import shutil
from src.file_chunker import split_file_into_chunks

def generate_test_file(size_mb):
    """Generate a temporary file of specified size."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        # Write random bytes to create a file of specified size
        temp_file.write(os.urandom(size_mb * 1024 * 1024))
        return temp_file.name

def test_split_file_into_chunks():
    # Generate a test file of 25MB
    test_file_path = generate_test_file(25)
    
    try:
        # Create a temporary directory for chunks
        temp_dir = tempfile.mkdtemp()
        
        # Split file into 10MB chunks
        chunk_files = split_file_into_chunks(
            test_file_path, 
            chunk_size_mb=10, 
            output_dir=temp_dir
        )
        
        # Verify chunk files
        assert len(chunk_files) == 3, "Should create 3 chunks for a 25MB file"
        
        # Check chunk sizes
        for chunk_file in chunk_files:
            assert os.path.exists(chunk_file), f"Chunk file {chunk_file} should exist"
            assert os.path.getsize(chunk_file) <= 10 * 1024 * 1024, "Chunk size should not exceed 10MB"
        
        # Verify total size matches original file
        total_chunk_size = sum(os.path.getsize(f) for f in chunk_files)
        original_size = os.path.getsize(test_file_path)
        assert total_chunk_size == original_size, "Total chunk size should match original file size"
    
    finally:
        # Clean up
        os.unlink(test_file_path)
        shutil.rmtree(temp_dir)

def test_invalid_file_path():
    with pytest.raises(FileNotFoundError):
        split_file_into_chunks('/path/to/nonexistent/file.txt')

def test_invalid_chunk_size():
    test_file_path = generate_test_file(5)
    
    try:
        with pytest.raises(ValueError):
            split_file_into_chunks(test_file_path, chunk_size_mb=0)
        with pytest.raises(ValueError):
            split_file_into_chunks(test_file_path, chunk_size_mb=-1)
    
    finally:
        os.unlink(test_file_path)

def test_custom_output_directory():
    test_file_path = generate_test_file(15)
    
    try:
        # Create a specific output directory
        custom_dir = tempfile.mkdtemp()
        
        chunk_files = split_file_into_chunks(
            test_file_path, 
            chunk_size_mb=5, 
            output_dir=custom_dir
        )
        
        # Verify chunks are in the custom directory
        assert all(f.startswith(custom_dir) for f in chunk_files), "Chunks should be in custom directory"
    
    finally:
        # Clean up
        os.unlink(test_file_path)
        shutil.rmtree(custom_dir)