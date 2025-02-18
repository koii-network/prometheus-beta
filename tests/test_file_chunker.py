import os
import pytest
import tempfile
import filecmp

from src.file_chunker import split_file_into_chunks

def test_split_file_basic():
    # Create a temporary file with known content
    with tempfile.NamedTemporaryFile(delete=False) as temp_input:
        input_filename = temp_input.name
        test_content = b'A' * (15 * 1024 * 1024)  # 15MB of data
        temp_input.write(test_content)
    
    try:
        # Create a temporary output directory
        with tempfile.TemporaryDirectory() as temp_dir:
            # Split the file into 10MB chunks
            chunk_files = split_file_into_chunks(
                input_file=input_filename, 
                chunk_size_mb=10, 
                output_dir=temp_dir
            )
            
            # Check chunks
            assert len(chunk_files) == 2, "Should create 2 chunks"
            
            # Verify chunk sizes
            chunk_sizes = [os.path.getsize(chunk) for chunk in chunk_files]
            assert chunk_sizes[0] == 10 * 1024 * 1024, "First chunk should be 10MB"
            assert chunk_sizes[1] == 5 * 1024 * 1024, "Second chunk should be 5MB"
    
    finally:
        # Clean up the input file
        os.unlink(input_filename)

def test_split_file_error_handling():
    # Test non-existent file
    with pytest.raises(FileNotFoundError):
        split_file_into_chunks("/path/to/nonexistent/file.txt")
    
    # Test invalid chunk size
    with tempfile.NamedTemporaryFile(delete=False) as temp_input:
        input_filename = temp_input.name
        with pytest.raises(ValueError):
            split_file_into_chunks(input_filename, chunk_size_mb=0)
        with pytest.raises(ValueError):
            split_file_into_chunks(input_filename, chunk_size_mb=-5)
    
    os.unlink(input_filename)

def test_split_file_custom_chunk_size():
    # Create a temporary file with known content
    with tempfile.NamedTemporaryFile(delete=False) as temp_input:
        input_filename = temp_input.name
        test_content = b'B' * (20 * 1024 * 1024)  # 20MB of data
        temp_input.write(test_content)
    
    try:
        # Create a temporary output directory
        with tempfile.TemporaryDirectory() as temp_dir:
            # Split the file into 7MB chunks
            chunk_files = split_file_into_chunks(
                input_file=input_filename, 
                chunk_size_mb=7, 
                output_dir=temp_dir
            )
            
            # Check chunks
            assert len(chunk_files) == 3, "Should create 3 chunks"
            
            # Verify chunk sizes
            chunk_sizes = [os.path.getsize(chunk) for chunk in chunk_files]
            assert all(size <= 7 * 1024 * 1024 for size in chunk_sizes), "Chunks should not exceed 7MB"
    
    finally:
        # Clean up the input file
        os.unlink(input_filename)