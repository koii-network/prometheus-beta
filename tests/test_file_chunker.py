import os
import pytest
import tempfile
from src.file_chunker import split_file_into_chunks

def test_split_file_basic():
    # Create a temporary file with known content
    with tempfile.NamedTemporaryFile(delete=False) as temp_input:
        input_content = b"0123456789" * 100  # 1000 bytes
        temp_input.write(input_content)
        temp_input.flush()
        input_path = temp_input.name
    
    try:
        # Split into 250-byte chunks
        chunk_files = split_file_into_chunks(input_path, 250)
        
        # Verify number of chunks
        assert len(chunk_files) == 4
        
        # Verify chunk contents
        for i, chunk_file in enumerate(chunk_files, 1):
            with open(chunk_file, 'rb') as f:
                chunk_content = f.read()
                assert len(chunk_content) <= 250
            
            # Clean up chunk file
            os.unlink(chunk_file)
    
    finally:
        # Clean up input file
        os.unlink(input_path)

def test_split_file_custom_output_dir():
    with tempfile.NamedTemporaryFile(delete=False) as temp_input:
        input_content = b"0123456789" * 100  # 1000 bytes
        temp_input.write(input_content)
        temp_input.flush()
        input_path = temp_input.name
    
    with tempfile.TemporaryDirectory() as temp_output_dir:
        try:
            # Split into 250-byte chunks with custom output directory
            chunk_files = split_file_into_chunks(input_path, 250, temp_output_dir)
            
            # Verify chunks are in the correct directory
            for chunk_file in chunk_files:
                assert os.path.dirname(chunk_file) == temp_output_dir
                
                # Clean up chunk file
                os.unlink(chunk_file)
        
        finally:
            # Clean up input file
            os.unlink(input_path)

def test_invalid_input_file():
    with pytest.raises(ValueError, match="does not exist"):
        split_file_into_chunks("/path/to/nonexistent/file", 100)

def test_invalid_chunk_size():
    with tempfile.NamedTemporaryFile(delete=False) as temp_input:
        temp_input.write(b"test content")
        temp_input.flush()
        input_path = temp_input.name
    
    try:
        # Test zero chunk size
        with pytest.raises(ValueError, match="Chunk size must be a positive integer"):
            split_file_into_chunks(input_path, 0)
        
        # Test negative chunk size
        with pytest.raises(ValueError, match="Chunk size must be a positive integer"):
            split_file_into_chunks(input_path, -100)
    
    finally:
        # Clean up input file
        os.unlink(input_path)

def test_empty_file():
    with tempfile.NamedTemporaryFile(delete=False) as temp_input:
        temp_input.write(b"")
        temp_input.flush()
        input_path = temp_input.name
    
    try:
        # Split empty file
        chunk_files = split_file_into_chunks(input_path, 100)
        
        # Verify no chunks created
        assert len(chunk_files) == 0
    
    finally:
        # Clean up input file
        os.unlink(input_path)