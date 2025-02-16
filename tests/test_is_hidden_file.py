import os
import pytest
from src.is_hidden_file import is_hidden_file

def test_unix_hidden_file():
    # Test files starting with dot
    assert is_hidden_file('/path/to/.hidden_file.txt') == True
    assert is_hidden_file('/path/to/.hidden_config') == True

def test_non_hidden_file():
    # Test normal files
    assert is_hidden_file('/path/to/normal_file.txt') == False
    assert is_hidden_file('regular_file') == False

def test_file_with_dot_in_middle():
    # Test files with dot in the middle (not hidden)
    assert is_hidden_file('/path/to/my.file.txt') == False

def test_edge_cases():
    # Test empty path and None
    assert is_hidden_file('') == False
    assert is_hidden_file(None) == False

def test_just_dot_file():
    # Test single dot files
    assert is_hidden_file('/path/to/.') == True
    assert is_hidden_file('/path/to/..') == True