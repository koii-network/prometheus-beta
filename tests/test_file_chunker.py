import os
import pytest
from src.file_chunker import chunk_file

def test_chunk_file_default_parameters(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_large_file.txt"
    with open(test_file, 'wb') as f:
        f.write(b'0' * (15 * 1024 * 1024))  # 15 MB file
    
    # Chunk the file
    chunks = chunk_file(str(test_file))
    
    # Assert chunks are created (default 10MB chunks)
    assert len(chunks) == 2
    for chunk in chunks:
        assert os.path.exists(chunk)
        chunk_size = os.path.getsize(chunk)
        assert chunk_size <= 10 * 1024 * 1024

def test_chunk_file_custom_chunk_size(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_large_file.txt"
    with open(test_file, 'wb') as f:
        f.write(b'0' * (15 * 1024 * 1024))  # 15 MB file
    
    # Chunk the file with 5MB chunks
    chunks = chunk_file(str(test_file), chunk_size_mb=5)
    
    # Assert chunks are created (5MB chunks)
    assert len(chunks) == 3
    for chunk in chunks:
        assert os.path.exists(chunk)
        chunk_size = os.path.getsize(chunk)
        assert chunk_size <= 5 * 1024 * 1024

def test_chunk_file_custom_output_dir(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_large_file.txt"
    with open(test_file, 'wb') as f:
        f.write(b'0' * (5 * 1024 * 1024))  # 5 MB file
    
    # Create a custom output directory
    output_dir = tmp_path / "chunks"
    
    # Chunk the file with custom output directory
    chunks = chunk_file(str(test_file), output_dir=str(output_dir))
    
    # Assert chunks are created in the specified directory
    assert len(chunks) > 0
    for chunk in chunks:
        assert chunk.startswith(str(output_dir))
        assert os.path.exists(chunk)

def test_chunk_file_empty_file(tmp_path):
    # Create an empty test file
    test_file = tmp_path / "empty_file.txt"
    with open(test_file, 'wb') as f:
        pass
    
    # Chunk the empty file
    chunks = chunk_file(str(test_file))
    
    # Assert no chunks are created
    assert len(chunks) == 0

def test_chunk_file_invalid_input():
    # Test non-existent file
    with pytest.raises(FileNotFoundError):
        chunk_file("/path/to/nonexistent/file.txt")

def test_chunk_file_invalid_chunk_size(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_file.txt"
    with open(test_file, 'wb') as f:
        f.write(b'test data')
    
    # Test invalid chunk sizes
    with pytest.raises(ValueError):
        chunk_file(str(test_file), chunk_size_mb=0)
    
    with pytest.raises(ValueError):
        chunk_file(str(test_file), chunk_size_mb=-1)