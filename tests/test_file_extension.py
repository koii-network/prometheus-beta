import pytest
from src.file_extension import get_file_extension

def test_get_file_extension_normal_cases():
    assert get_file_extension('document.txt') == 'txt'
    assert get_file_extension('/path/to/image.jpg') == 'jpg'
    assert get_file_extension('script.py') == 'py'

def test_get_file_extension_no_extension():
    assert get_file_extension('filename') == ''
    assert get_file_extension('/path/to/file') == ''

def test_get_file_extension_multiple_dots():
    assert get_file_extension('archive.tar.gz') == 'gz'
    assert get_file_extension('document.backup.txt') == 'txt'

def test_get_file_extension_hidden_files():
    assert get_file_extension('.gitignore') == ''
    assert get_file_extension('/path/to/.bashrc') == ''

def test_get_file_extension_error_handling():
    with pytest.raises(TypeError):
        get_file_extension(None)
    with pytest.raises(TypeError):
        get_file_extension(123)
    with pytest.raises(TypeError):
        get_file_extension(['file.txt'])