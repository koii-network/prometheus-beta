import pytest
from src.file_extension import get_file_extension

def test_get_file_extension_normal_cases():
    # Test various normal file paths
    assert get_file_extension('document.txt') == 'txt'
    assert get_file_extension('/path/to/image.jpg') == 'jpg'
    assert get_file_extension('script.py') == 'py'
    assert get_file_extension('README.md') == 'md'

def test_get_file_extension_edge_cases():
    # Test edge cases
    assert get_file_extension('filename') == ''  # No extension
    assert get_file_extension('.gitignore') == ''  # Hidden file
    assert get_file_extension('document.TXT') == 'txt'  # Case insensitivity

def test_get_file_extension_error_cases():
    # Test error cases
    with pytest.raises(TypeError):
        get_file_extension(None)
    with pytest.raises(TypeError):
        get_file_extension(123)
    with pytest.raises(TypeError):
        get_file_extension(['file.txt'])