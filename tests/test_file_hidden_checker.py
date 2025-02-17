import os
import pytest
from src.file_hidden_checker import is_hidden_file

def test_unix_hidden_file():
    # Test files starting with a dot
    assert is_hidden_file('/path/to/.hidden_file.txt') == True
    assert is_hidden_file('/path/to/.config') == True

def test_non_hidden_file():
    # Test regular files
    assert is_hidden_file('/path/to/normal_file.txt') == False
    assert is_hidden_file('regular_file') == False

def test_edge_cases():
    # Test empty path
    assert is_hidden_file('') == False
    
    # Test None input
    with pytest.raises(TypeError):
        is_hidden_file(None)

def test_just_dot_file():
    # Test files that are just a dot
    assert is_hidden_file('/path/to/.') == True
    assert is_hidden_file('/path/to/..') == True