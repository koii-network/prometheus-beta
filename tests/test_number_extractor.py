import sys
import os
import pytest

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from number_extractor import extract_numbers

def test_extract_numbers():
    # Test with various input scenarios
    assert extract_numbers("hello 123 world") == [123]
    assert extract_numbers("pi is 3.14 and e is 2.718") == [3.14, 2.718]
    assert extract_numbers("no numbers here") == []
    assert extract_numbers("-42 and 17.5") == [-42, 17.5]
    assert extract_numbers("multiple 10 numbers 20 in 30 a 40 string 50") == [10, 20, 30, 40, 50]

def test_extract_numbers_edge_cases():
    # Test edge cases
    assert extract_numbers("") == []
    assert extract_numbers("only text") == []
    assert extract_numbers("negative -10.5 and positive 15.7") == [-10.5, 15.7]

def test_extract_numbers_complex():
    # Test more complex scenarios
    assert extract_numbers("temp: -5.6 degrees") == [-5.6]
    assert extract_numbers("score: 100 points, bonus: 25.5") == [100, 25.5]
    assert extract_numbers("mix -123 and 456.789 numbers") == [-123, 456.789]