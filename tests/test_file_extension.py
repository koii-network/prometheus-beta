import pytest
import os
from src.file_extension import get_file_extension

def test_get_file_extension_normal_files():
    """Test getting extensions for various file names"""
    assert get_file_extension('document.txt') == 'txt'
    assert get_file_extension('image.jpg') == 'jpg'
    assert get_file_extension('script.py') == 'py'
    assert get_file_extension('archive.tar.gz') == 'gz'

def test_get_file_extension_no_extension():
    """Test files without extensions"""
    assert get_file_extension('README') == ''
    assert get_file_extension('filename_without_ext') == ''

def test_get_file_extension_hidden_files():
    """Test hidden files with and without extensions"""
    assert get_file_extension('.gitignore') == ''
    assert get_file_extension('.env.local') == 'local'

def test_get_file_extension_full_paths():
    """Test file extensions with full file paths"""
    assert get_file_extension('/home/user/documents/report.pdf') == 'pdf'
    assert get_file_extension('C:\\Users\\name\\Desktop\\file.docx') == 'docx'

def test_get_file_extension_invalid_input():
    """Test invalid input types"""
    with pytest.raises(TypeError):
        get_file_extension(123)
    with pytest.raises(TypeError):
        get_file_extension(None)
    with pytest.raises(TypeError):
        get_file_extension(['file.txt'])