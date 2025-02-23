"""
Tests for the file extension extraction function.
"""

import pytest
import os
from src.file_extension import get_file_extension


def test_standard_file_extensions():
    """Test common file extensions."""
    assert get_file_extension('document.txt') == '.txt'
    assert get_file_extension('image.jpg') == '.jpg'
    assert get_file_extension('script.py') == '.py'
    assert get_file_extension('data.csv') == '.csv'


def test_file_with_multiple_dots():
    """Test files with multiple dots in the name."""
    assert get_file_extension('complex.file.name.txt') == '.txt'
    assert get_file_extension('archive.tar.gz') == '.gz'


def test_files_without_extension():
    """Test files without any extension."""
    assert get_file_extension('no_extension_file') == ''
    assert get_file_extension('/path/to/no_extension') == ''


def test_full_path_files():
    """Test file extensions with full file paths."""
    assert get_file_extension('/home/user/documents/report.pdf') == '.pdf'
    assert get_file_extension('C:\\Users\\Name\\file.docx') == '.docx'


def test_edge_cases():
    """Test various edge cases."""
    assert get_file_extension('.hidden_file') == ''
    assert get_file_extension('file.') == '.'
    assert get_file_extension('') == ''


def test_input_types():
    """Ensure the function handles different input types gracefully."""
    with pytest.raises(TypeError):
        get_file_extension(None)
    with pytest.raises(TypeError):
        get_file_extension(123)