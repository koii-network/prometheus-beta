import os
import pytest
import tempfile
import shutil

from src.file_chunker import split_file_into_chunks

def create_test_file(size_mb):
    """Create a temporary file of specified size."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(os.urandom(size_mb * 1024 * 1024))
        return temp_file.name

def test_split_file_basic():
    """Test basic file splitting functionality."""
    input_file = create_test_file(25)  # 25 MB file
    try:
        chunks = split_file_into_chunks(input_file, chunk_size_mb=10)
        
        # Check number of chunks
        assert len(chunks) == 3, f"Expected 3 chunks, got {len(chunks)}"
        
        # Verify chunk files exist
        for chunk in chunks:
            assert os.path.exists(chunk), f"Chunk file {chunk} does not exist"
            
        # Verify chunk sizes
        chunk_sizes = [os.path.getsize(chunk) for chunk in chunks]
        assert all(0 < size <= 10 * 1024 * 1024 for size in chunk_sizes), "Chunk sizes are incorrect"
    
    finally:
        # Clean up: remove the original file and chunks
        os.unlink(input_file)
        for chunk in chunks:
            os.unlink(chunk)

def test_split_file_custom_output_dir():
    """Test splitting file with a custom output directory."""
    input_file = create_test_file(15)
    temp_dir = tempfile.mkdtemp()
    try:
        chunks = split_file_into_chunks(input_file, chunk_size_mb=5, output_dir=temp_dir)
        
        # Check chunks are in the specified directory
        assert all(chunk.startswith(temp_dir) for chunk in chunks), "Chunks not in specified directory"
    
    finally:
        # Clean up
        os.unlink(input_file)
        shutil.rmtree(temp_dir)

def test_split_file_nonexistent_input():
    """Test handling of non-existent input file."""
    with pytest.raises(FileNotFoundError):
        split_file_into_chunks("/path/to/nonexistent/file.txt")

def test_split_file_invalid_chunk_size():
    """Test handling of invalid chunk sizes."""
    input_file = create_test_file(10)
    try:
        with pytest.raises(ValueError):
            split_file_into_chunks(input_file, chunk_size_mb=0)
        
        with pytest.raises(ValueError):
            split_file_into_chunks(input_file, chunk_size_mb=-5)
    
    finally:
        os.unlink(input_file)

def test_split_file_small_file():
    """Test splitting a small file."""
    input_file = create_test_file(5)
    try:
        chunks = split_file_into_chunks(input_file, chunk_size_mb=10)
        
        # Should create just one chunk
        assert len(chunks) == 1, f"Expected 1 chunk, got {len(chunks)}"
    
    finally:
        os.unlink(input_file)
        for chunk in chunks:
            os.unlink(chunk)