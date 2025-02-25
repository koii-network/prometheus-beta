import pytest
from src.file_extension import get_file_extension

def test_get_file_extension_valid_paths():
    # Test various file paths with different extensions
    assert get_file_extension('document.txt') == 'txt'
    assert get_file_extension('/path/to/image.jpg') == 'jpg'
    assert get_file_extension('script.py') == 'py'
    assert get_file_extension('README.md') == 'md'

def test_get_file_extension_no_extension():
    # Test files without extensions
    assert get_file_extension('filename') == ''
    assert get_file_extension('/path/to/file') == ''

def test_get_file_extension_multiple_dots():
    # Test files with multiple dots
    assert get_file_extension('archive.tar.gz') == 'gz'
    assert get_file_extension('document.backup.txt') == 'txt'

def test_get_file_extension_edge_cases():
    # Test files with dot at the start or only dot
    assert get_file_extension('.gitignore') == ''
    assert get_file_extension('hidden.file') == 'file'

def test_get_file_extension_invalid_input():
    # Test invalid input types
    with pytest.raises(TypeError):
        get_file_extension(None)
    with pytest.raises(TypeError):
        get_file_extension(123)
    with pytest.raises(TypeError):
        get_file_extension(['file.txt'])