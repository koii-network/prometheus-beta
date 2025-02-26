import pytest
from src.shannon_fano_coding import (
    calculate_frequencies, 
    sort_symbols_by_frequency, 
    split_group, 
    generate_shannon_fano_codes,
    shannon_fano_encode,
    shannon_fano_decode
)

def test_calculate_frequencies():
    """Test frequency calculation."""
    data = "hello world"
    frequencies = calculate_frequencies(data)
    assert frequencies == {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

def test_sort_symbols_by_frequency():
    """Test sorting symbols by frequency."""
    frequencies = {'a': 5, 'b': 2, 'c': 8}
    sorted_symbols = sort_symbols_by_frequency(frequencies)
    assert sorted_symbols == [('c', 8), ('a', 5), ('b', 2)]

def test_split_group():
    """Test splitting group of symbols."""
    sorted_symbols = [('c', 8), ('a', 5), ('b', 2), ('d', 1)]
    group1, group2 = split_group(sorted_symbols)
    assert group1 == [('c', 8), ('a', 5)]
    assert group2 == [('b', 2), ('d', 1)]

def test_generate_shannon_fano_codes():
    """Test generating Shannon-Fano codes."""
    sorted_symbols = [('c', 8), ('a', 5), ('b', 2), ('d', 1)]
    codes = generate_shannon_fano_codes(sorted_symbols)
    assert set(codes.keys()) == {'c', 'a', 'b', 'd'}
    assert len(set(codes.values())) == 4  # Unique codes

def test_shannon_fano_encode_decode():
    """Test complete encode and decode process."""
    original_data = "hello world"
    codes, encoded_data = shannon_fano_encode(original_data)
    
    # Verify encoding
    decoded_data = shannon_fano_decode(codes, encoded_data)
    assert decoded_data == original_data

def test_shannon_fano_encode_decode_empty_string():
    """Test encoding and decoding an empty string."""
    original_data = ""
    codes, encoded_data = shannon_fano_encode(original_data)
    decoded_data = shannon_fano_decode(codes, encoded_data)
    assert decoded_data == original_data

def test_shannon_fano_encode_decode_repeated_chars():
    """Test encoding and decoding with repeated characters."""
    original_data = "aaabbbcccddd"
    codes, encoded_data = shannon_fano_encode(original_data)
    decoded_data = shannon_fano_decode(codes, encoded_data)
    assert decoded_data == original_data

def test_invalid_decode():
    """Test decoding with invalid encoded data."""
    codes = {'a': '0', 'b': '1'}
    with pytest.raises(ValueError, match="Invalid encoded data: incomplete code"):
        shannon_fano_decode(codes, "01010")  # Incomplete last code