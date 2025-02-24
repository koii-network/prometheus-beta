import os
import pytest
import tempfile
import shutil
from src.file_chunker import split_file_into_chunks

def test_split_file_into_chunks():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a test file
        test_file_path = os.path.join(temp_dir, 'test_large_file.txt')
        with open(test_file_path, 'wb') as f:
            # Create a 25MB file
            f.write(b'0' * (25 * 1024 * 1024))
        
        # Split the file
        chunk_files = split_file_into_chunks(test_file_path, chunk_size_mb=10)
        
        # Verify chunk files
        assert len(chunk_files) == 3, "Should create 3 chunks for a 25MB file when chunk size is 10MB"
        
        # Check chunk files exist and have correct sizes
        for chunk_file in chunk_files:
            assert os.path.exists(chunk_file), f"Chunk file {chunk_file} should exist"
            chunk_size = os.path.getsize(chunk_file)
            assert chunk_size <= 10 * 1024 * 1024, f"Chunk {chunk_file} should not exceed 10MB"

def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        split_file_into_chunks('non_existent_file.txt')

def test_invalid_chunk_size():
    with tempfile.TemporaryDirectory() as temp_dir:
        test_file_path = os.path.join(temp_dir, 'test_file.txt')
        with open(test_file_path, 'w') as f:
            f.write('test content')
        
        with pytest.raises(ValueError):
            split_file_into_chunks(test_file_path, chunk_size_mb=0)
        
        with pytest.raises(ValueError):
            split_file_into_chunks(test_file_path, chunk_size_mb=-5)

def test_custom_output_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a test file
        test_file_path = os.path.join(temp_dir, 'test_large_file.txt')
        with open(test_file_path, 'wb') as f:
            # Create a 15MB file
            f.write(b'0' * (15 * 1024 * 1024))
        
        # Custom output directory
        custom_output_dir = os.path.join(temp_dir, 'chunks')
        
        # Split the file
        chunk_files = split_file_into_chunks(test_file_path, chunk_size_mb=10, output_dir=custom_output_dir)
        
        # Verify chunks are in the custom directory
        assert len(chunk_files) == 2
        for chunk_file in chunk_files:
            assert chunk_file.startswith(custom_output_dir)
            assert os.path.exists(chunk_file)