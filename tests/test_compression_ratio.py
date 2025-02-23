import os
import pytest
import tempfile
from src.compression_ratio import calculate_compression_ratio

def test_calculate_compression_ratio():
    # Create temporary files for testing
    with tempfile.TemporaryDirectory() as tmpdir:
        # Original file
        original_path = os.path.join(tmpdir, 'original.txt')
        with open(original_path, 'w') as f:
            f.write('A' * 1000)  # 1000 bytes
        
        # Compressed file (simulated)
        compressed_path = os.path.join(tmpdir, 'compressed.txt')
        with open(compressed_path, 'w') as f:
            f.write('A' * 500)  # 500 bytes
        
        # Test compression ratio calculation
        ratio = calculate_compression_ratio(original_path, compressed_path)
        assert ratio == 2.0  # 1000 / 500 = 2.0

def test_non_existent_files():
    with pytest.raises(FileNotFoundError):
        calculate_compression_ratio('non_existent_original.txt', 'non_existent_compressed.txt')

def test_zero_size_files():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create empty files
        original_path = os.path.join(tmpdir, 'empty_original.txt')
        compressed_path = os.path.join(tmpdir, 'empty_compressed.txt')
        
        open(original_path, 'w').close()
        open(compressed_path, 'w').close()
        
        with pytest.raises(ValueError, match="Original file size must be greater than 0"):
            calculate_compression_ratio(original_path, compressed_path)

def test_compressed_larger_than_original():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Original file
        original_path = os.path.join(tmpdir, 'original.txt')
        with open(original_path, 'w') as f:
            f.write('A' * 500)  # 500 bytes
        
        # Compressed file (larger)
        compressed_path = os.path.join(tmpdir, 'compressed.txt')
        with open(compressed_path, 'w') as f:
            f.write('A' * 1000)  # 1000 bytes
        
        with pytest.raises(ValueError, match="Compressed file size cannot be larger than original file size"):
            calculate_compression_ratio(original_path, compressed_path)

def test_decimal_compression_ratio():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Original file
        original_path = os.path.join(tmpdir, 'original.txt')
        with open(original_path, 'w') as f:
            f.write('A' * 1000)  # 1000 bytes
        
        # Compressed file with non-exact division
        compressed_path = os.path.join(tmpdir, 'compressed.txt')
        with open(compressed_path, 'w') as f:
            f.write('A' * 333)  # 333 bytes
        
        ratio = calculate_compression_ratio(original_path, compressed_path)
        assert ratio == 3.00  # Rounded to 2 decimal places