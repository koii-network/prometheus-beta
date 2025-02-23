"""
Tests for the file_extension utility function.
"""

import pytest
from src.file_extension import get_file_extension


def test_get_file_extension_normal_cases():
    """Test getting extensions for various normal file paths."""
    assert get_file_extension('document.txt') == 'txt'
    assert get_file_extension('image.jpg') == 'jpg'
    assert get_file_extension('script.py') == 'py'
    assert get_file_extension('archive.tar.gz') == 'gz'


def test_get_file_extension_mixed_case():
    """Test that extensions are converted to lowercase."""
    assert get_file_extension('file.PDF') == 'pdf'
    assert get_file_extension('FILE.TXT') == 'txt'


def test_get_file_extension_with_path():
    """Test getting extensions from full file paths."""
    assert get_file_extension('/home/user/document.txt') == 'txt'
    assert get_file_extension('C:\\Users\\name\\file.docx') == 'docx'


def test_get_file_extension_no_extension():
    """Test handling of files without extensions."""
    assert get_file_extension('README') == ''
    assert get_file_extension('filename_without_ext') == ''


def test_get_file_extension_hidden_files():
    """Test handling of hidden files."""
    assert get_file_extension('.gitignore') == ''
    assert get_file_extension('/.dockerignore') == ''


def test_get_file_extension_invalid_input():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        get_file_extension(None)
    with pytest.raises(TypeError):
        get_file_extension(123)
    with pytest.raises(TypeError):
        get_file_extension(['file.txt'])