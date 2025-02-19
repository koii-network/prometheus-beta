import os
import gzip
import pytest
import tempfile
from src.gzip_compression import compress_file

def test_compress_file_basic():
    # Create a temporary input file
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp_input:
        temp_input.write("This is a test file for compression")
        input_path = temp_input.name
    
    try:
        # Compress the file
        output_path = compress_file(input_path)
        
        # Verify compressed file exists
        assert os.path.exists(output_path)
        assert output_path.endswith('.gz')
        
        # Verify compression worked by trying to decompress
        with gzip.open(output_path, 'rt') as f:
            content = f.read()
            assert content == "This is a test file for compression"
    
    finally:
        # Clean up temporary files
        os.unlink(input_path)
        if os.path.exists(output_path):
            os.unlink(output_path)

def test_compress_file_custom_output():
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp_input:
        temp_input.write("Custom output path test")
        input_path = temp_input.name
    
    custom_output = input_path + '.custom.gz'
    
    try:
        output_path = compress_file(input_path, custom_output)
        
        assert output_path == custom_output
        assert os.path.exists(output_path)
        
        with gzip.open(output_path, 'rt') as f:
            content = f.read()
            assert content == "Custom output path test"
    
    finally:
        os.unlink(input_path)
        if os.path.exists(custom_output):
            os.unlink(custom_output)

def test_compress_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        compress_file('/path/to/nonexistent/file.txt')

def test_compress_without_write_permission(tmp_path):
    # Create a read-only file
    test_file = tmp_path / 'readonly.txt'
    test_file.write_text('test content')
    test_file.chmod(0o444)  # Read-only
    
    with pytest.raises(PermissionError):
        compress_file(str(test_file), str(tmp_path / 'output.gz'))