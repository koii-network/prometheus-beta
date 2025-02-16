import os
import pytest
import tempfile
from src.compression_ratio import calculate_compression_ratio

def test_calculate_compression_ratio_empty_file():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.close()
        try:
            ratio = calculate_compression_ratio(temp_file.name)
            assert ratio == 1.0
        finally:
            os.unlink(temp_file.name)

def test_calculate_compression_ratio_text_file():
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write('Hello' * 1000)  # Repeatable content for consistent compression
        temp_file.close()
        try:
            ratio = calculate_compression_ratio(temp_file.name)
            assert ratio > 1.0  # Compression should reduce size
        finally:
            os.unlink(temp_file.name)

def test_calculate_compression_ratio_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        calculate_compression_ratio('/path/to/nonexistent/file.txt')

def test_calculate_compression_ratio_zero_byte_file():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.truncate(0)
        temp_file.close()
        try:
            ratio = calculate_compression_ratio(temp_file.name)
            assert ratio == 1.0
        finally:
            os.unlink(temp_file.name)

def test_calculate_compression_ratio_minimum_ratio():
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write('Uncompressible' * 100)
        temp_file.close()
        try:
            ratio = calculate_compression_ratio(temp_file.name)
            assert ratio >= 1.0
        finally:
            os.unlink(temp_file.name)