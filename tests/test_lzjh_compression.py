import pytest
from src.lzjh_compression import lzjh_compress

def test_lzjh_compress_basic():
    """Test basic compression functionality"""
    input_data = "ABABABABABABABAB"
    compressed = lzjh_compress(input_data)
    assert len(compressed) < len(input_data)
    assert 256 in compressed  # Check for dictionary encoding

def test_lzjh_compress_empty_input():
    """Test compression with empty input"""
    input_data = ""
    compressed = lzjh_compress(input_data)
    assert compressed == []

def test_lzjh_compress_single_character():
    """Test compression with single character"""
    input_data = "A"
    compressed = lzjh_compress(input_data)
    assert compressed == [ord('A')]

def test_lzjh_compress_bytes_input():
    """Test compression with bytes input"""
    input_data = b'\x01\x02\x03\x01\x02\x03'
    compressed = lzjh_compress(input_data)
    assert len(compressed) < len(input_data)
    assert 256 in compressed  # Check for dictionary encoding

def test_lzjh_compress_repetitive_pattern():
    """Test compression with highly repetitive input"""
    input_data = "HAHAHAHAHAHAHAHA"
    compressed = lzjh_compress(input_data)
    assert len(compressed) < len(input_data)
    assert all(isinstance(x, int) for x in compressed)

def test_lzjh_compress_unicode():
    """Test compression with unicode input"""
    input_data = "こんにちは、世界"
    compressed = lzjh_compress(input_data)
    assert len(compressed) < len(input_data.encode('utf-8'))
    assert all(isinstance(x, int) for x in compressed)