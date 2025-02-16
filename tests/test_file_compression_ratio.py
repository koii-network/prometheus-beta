import os
import pytest
import tempfile
from src.file_compression_ratio import calculate_compression_ratio

def test_compression_ratio_text_file():
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Hello world!" * 100)  # Repetitive text for better compression
        temp_file.close()
        
        try:
            ratio = calculate_compression_ratio(temp_file.name)
            assert ratio > 1.0, "Compression ratio should be greater than 1"
        finally:
            os.unlink(temp_file.name)

def test_compression_ratio_binary_file():
    with tempfile.NamedTemporaryFile(mode='wb', delete=False) as temp_file:
        temp_file.write(os.urandom(1024))  # Random binary data
        temp_file.close()
        
        try:
            ratio = calculate_compression_ratio(temp_file.name)
            assert ratio >= 1.0, "Compression ratio should be at least 1"
        finally:
            os.unlink(temp_file.name)

def test_empty_file_raises_error():
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.close()
        
        try:
            with pytest.raises(ValueError, match="Cannot calculate compression ratio for an empty file"):
                calculate_compression_ratio(temp_file.name)
        finally:
            os.unlink(temp_file.name)

def test_nonexistent_file_raises_error():
    with pytest.raises(FileNotFoundError):
        calculate_compression_ratio("/path/to/nonexistent/file.txt")

def test_unreadable_file_raises_error():
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.close()
        # Remove read permissions
        os.chmod(temp_file.name, 0o000)
        
        try:
            with pytest.raises(ValueError, match="Error reading file"):
                calculate_compression_ratio(temp_file.name)
        finally:
            # Restore permissions and delete
            os.chmod(temp_file.name, 0o644)
            os.unlink(temp_file.name)