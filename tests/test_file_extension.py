"""
Tests for the file_extension module.
"""

import pytest
from src.file_extension import get_file_extension


def test_standard_file_extension():
    """Test getting extension from a standard file path."""
    assert get_file_extension('document.txt') == 'txt'
    assert get_file_extension('/path/to/file.py') == 'py'


def test_file_with_multiple_dots():
    """Test files with multiple dots in the name."""
    assert get_file_extension('archive.tar.gz') == 'gz'
    assert get_file_extension('user.profile.jpg') == 'jpg'


def test_file_without_extension():
    """Test files without an extension."""
    assert get_file_extension('README') == ''
    assert get_file_extension('/path/to/file_no_ext') == ''


def test_extension_with_leading_dot():
    """Test files with leading dot scenarios."""
    assert get_file_extension('.gitignore') == ''
    assert get_file_extension('config/.env') == ''  # Changed from 'env' to ''


def test_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError, match="Input must be a string"):
        get_file_extension(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        get_file_extension(123)


def test_empty_string():
    """Test handling of empty string input."""
    assert get_file_extension('') == ''