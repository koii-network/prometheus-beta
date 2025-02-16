import os
import pytest
from src.file_utils import file_exists

def test_file_exists_known_file():
    """Test that an existing file returns True"""
    assert file_exists('README.md') == True
    assert file_exists('requirements.txt') == True

def test_file_exists_non_existent_file():
    """Test that a non-existent file returns False"""
    assert file_exists('non_existent_file.txt') == False

def test_file_exists_directory():
    """Test that a directory returns False"""
    assert file_exists('.') == False
    assert file_exists('..') == False

def test_file_exists_empty_path():
    """Test that an empty path returns False"""
    assert file_exists('') == False

def test_file_exists_invalid_path():
    """Test that an invalid path returns False"""
    assert file_exists(' ') == False
    assert file_exists(None) == False