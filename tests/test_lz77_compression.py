import pytest
from src.lz77_compression import LZ77Compressor

def test_lz77_compression_empty_input():
    compressor = LZ77Compressor()
    assert compressor.compress("") == []
    assert compressor.decompress([]) == b""

def test_lz77_compression_simple_string():
    compressor = LZ77Compressor()
    text = "HELLO WORLD"
    compressed = compressor.compress(text)
    decompressed = compressor.decompress(compressed)
    assert decompressed.decode('utf-8') == text

def test_lz77_compression_repeated_pattern():
    compressor = LZ77Compressor()
    text = "ABCABCABCABC"
    compressed = compressor.compress(text)
    decompressed = compressor.decompress(compressed)
    assert decompressed.decode('utf-8') == text

def test_lz77_compression_bytes():
    compressor = LZ77Compressor()
    data = b'\x01\x02\x03\x01\x02\x03\x04\x05'
    compressed = compressor.compress(data)
    decompressed = compressor.decompress(compressed)
    assert decompressed == data

def test_lz77_compression_long_repeated_sequence():
    compressor = LZ77Compressor()
    text = "Hello " * 100
    compressed = compressor.compress(text)
    decompressed = compressor.decompress(compressed)
    assert decompressed.decode('utf-8') == text

def test_lz77_compression_custom_window_size():
    compressor = LZ77Compressor(window_size=128, lookahead_buffer_size=32)
    text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 10
    compressed = compressor.compress(text)
    decompressed = compressor.decompress(compressed)
    assert decompressed.decode('utf-8') == text